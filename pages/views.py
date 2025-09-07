from django.shortcuts import render
from .models import Carro

def car_list(request):
    carros = Carro.objects.all().order_by('-fecha_creacion')
    return render(request, 'pages/car_list.html', {'carros': carros})
