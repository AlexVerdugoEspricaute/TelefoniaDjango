from django.contrib import admin
from .models import Llamada

class LlamadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'fecha', 'hora_inicio', 'hora_fin', 'precio', 'user')
    search_fields = ['numero', 'user__username']  # Agrega campos por los que puedes buscar

# Registrar el modelo Llamada junto con la clase LlamadaAdmin
admin.site.register(Llamada, LlamadaAdmin)
