from django.db import models
from django.contrib.auth.models import User

class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen_url = models.CharField(max_length=500, blank=True)  #  Cambiar a CharField
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
    
    def precio_formateado(self):
        return f"R$ {self.precio:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
