from django.contrib import admin
from .models import Carro

class CarroAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'año', 'precio_formateado']
    list_filter = ['marca', 'año']
    search_fields = ['marca', 'modelo']

admin.site.register(Carro, CarroAdmin)
