from django.db import models
from django.contrib.auth.models import User

class Mensagem(models.Model):
    remetente = models.ForeignKey(User, related_name='mensagens_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensagens_recebidas', on_delete=models.CASCADE)
    assunto = models.CharField(max_length=200)
    corpo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.assunto} - {self.remetente} para {self.destinatario}"
    
    class Meta:
        ordering = ['-data_envio']
