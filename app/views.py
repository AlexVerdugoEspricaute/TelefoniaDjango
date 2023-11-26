from django.shortcuts import render, redirect
from .models import Llamada
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from decimal import Decimal


@login_required
def home(request):
    # Obtener todas las llamadas asociadas al usuario autenticado
    llamadas = Llamada.objects.filter(user=request.user)
    # Calcular el valor total sumando los precios de todas las llamadas
    valor_total = llamadas.aggregate(Sum('precio'))['precio__sum'] or Decimal('0')

    data = {
    'llamadas': llamadas,
    'valor_total': valor_total,
}
    # Renderizar la página de inicio con la lista de llamadas del usuario
    return render(request, 'home.html', data)


def registro(request):
    # Inicializar el formulario de registro de usuario
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        # Procesar el formulario de registro cuando se envía
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            # Guardar el nuevo usuario y autenticarlo
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            # Redirigir al usuario a la página de inicio después del registro exitoso
            return redirect(to="home")
        data["form"] = formulario
    # Renderizar la página de registro con el formulario correspondiente
    return render(request, 'registration/registro.html', data)



@login_required
def boleta(request):
    # Obtener todas las llamadas asociadas al usuario autenticado
    llamadas = Llamada.objects.filter(user=request.user)

    # Calcular el valor neto sumando los precios de todas las llamadas y descontando el IVA
    valor_neto = llamadas.aggregate(Sum('precio'))['precio__sum'] or Decimal('0')
    iva_porcentaje = Decimal('0.19')
    valor_iva = valor_neto * iva_porcentaje

    # Calcular el valor neto restando el valor del IVA al total de las llamadas
    valor_neto -= valor_iva

    # Calcular el valor total sumando el valor neto y el IVA
    valor_total = valor_neto + valor_iva

    # Redondear los valores para tener dos decimales en la salida
    valor_neto = valor_neto.quantize(Decimal('0.00'))
    valor_iva = valor_iva.quantize(Decimal('0.00'))
    valor_total = valor_total.quantize(Decimal('0.00'))

    # Renderizar la página de la boleta con los valores calculados
    return render(request, 'boleta.html', {
        'valor_neto': valor_neto,
        'valor_iva': valor_iva,
        'valor_total': valor_total
    })
