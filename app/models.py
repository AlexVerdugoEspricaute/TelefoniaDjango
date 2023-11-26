from django.db import models
from django.contrib.auth.models import User

class Llamada(models.Model):
    # Campo para almacenar el número de la llamada
    numero = models.CharField(max_length=15)
    
    # Campo para almacenar la fecha de la llamada
    fecha = models.DateField()
    
    # Campo para almacenar la hora de inicio de la llamada
    hora_inicio = models.TimeField()
    
    # Campo para almacenar la hora de finalización de la llamada
    hora_fin = models.TimeField()
    
    # Campo para almacenar el precio de la llamada con precisión decimal
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Relación con el modelo de usuario de Django para asociar cada llamada a un usuario
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    # Método para representar el objeto como una cadena (string)
    def __str__(self):
        return self.numero
