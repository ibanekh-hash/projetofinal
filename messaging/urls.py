from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [
    path('', views.message_list, name='message_list'),
    path('nova/', views.nova_mensagem, name='nova_mensagem'),
    path('<int:mensagem_id>/', views.ver_mensagem, name='ver_mensagem'),
]
