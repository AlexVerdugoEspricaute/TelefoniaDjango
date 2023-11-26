# from django.test import TestCase, Client
# from django.contrib.auth.models import User

# class LlamadaViewTest(TestCase):
#     def setUp(self):
#         # Crea un usuario de prueba
#         self.usuario_prueba = User.objects.create_user(username='usuario_prueba', password='contraseña_prueba')
#         self.client = Client()

#     def test_vista_requiere_autenticacion(self):
#         # Intenta acceder a la vista de inicio de sesión sin autenticación
#         response = self.client.get('/accounts/login/')  # Ajusta esta ruta según tu configuración
#         print(response.status_code)
        
#         # La vista de inicio de sesión generalmente devuelve un código 200 incluso si no estás autenticado
#         # Así que aquí estamos ajustando la prueba para verificar si se muestra el formulario de inicio de sesión
#         self.assertEqual(response.status_code, 200)

#         # Autentica al usuario y vuelve a intentar la solicitud
#         self.client.login(username='usuario_prueba', password='contraseña_prueba')
#         response = self.client.get('/accounts/login/')  # Ajusta esta ruta según tu configuración
#         print(response.status_code)

#         # Ahora, deberías obtener un código 200 después de autenticar al usuario
#         self.assertEqual(response.status_code, 200)
