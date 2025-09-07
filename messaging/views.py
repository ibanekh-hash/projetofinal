from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Mensagem

@login_required
def message_list(request):
    mensagens_recebidas = Mensagem.objects.filter(destinatario=request.user).order_by('-data_envio')
    mensagens_enviadas = Mensagem.objects.filter(remetente=request.user).order_by('-data_envio')
    
    return render(request, 'messaging/message_list.html', {
        'mensagens_recebidas': mensagens_recebidas,
        'mensagens_enviadas': mensagens_enviadas
    })

@login_required
def nova_mensagem(request):
    if request.method == 'POST':
        destinatario_id = request.POST.get('destinatario')
        assunto = request.POST.get('assunto')
        corpo = request.POST.get('corpo')
        
        if destinatario_id and assunto and corpo:
            destinatario = User.objects.get(id=destinatario_id)
            Mensagem.objects.create(
                remetente=request.user,
                destinatario=destinatario,
                assunto=assunto,
                corpo=corpo
            )
            return redirect('messaging:message_list')
    
    usuarios = User.objects.exclude(id=request.user.id)
    return render(request, 'messaging/nova_mensagem.html', {'usuarios': usuarios})

@login_required
def ver_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, id=mensagem_id, destinatario=request.user)
    mensagem.lida = True
    mensagem.save()
    
    return render(request, 'messaging/ver_mensagem.html', {'mensagem': mensagem})
