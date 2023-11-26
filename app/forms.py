from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    # Clase de formulario personalizado que hereda de UserCreationForm

    class Meta:
        # La clase Meta proporciona metadatos adicionales para el formulario
        model = User  # Especifica el modelo de usuario asociado al formulario
        fields = ['username', 'email', 'password1', 'password2']  
        # Especifica los campos que se mostrarán en el formulario y su orden

    # Puedes añadir métodos adicionales o personalizaciones del formulario aquí si es necesario
