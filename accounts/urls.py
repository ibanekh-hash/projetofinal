from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.profile, name='profile'),
    path('registrar/', views.register, name='registrar'),
    path('entrar/', views.user_login, name='entrar'),
    path('sair/', views.user_logout, name='sair'),
]
