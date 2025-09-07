from django.contrib import admin
from .models import Mensagem

class MensagemAdmin(admin.ModelAdmin):
    list_display = ['assunto', 'remetente', 'destinatario', 'data_envio', 'lida']
    list_filter = ['data_envio', 'lida']
    search_fields = ['assunto', 'remetente__username', 'destinatario__username']

admin.site.register(Mensagem, MensagemAdmin)
