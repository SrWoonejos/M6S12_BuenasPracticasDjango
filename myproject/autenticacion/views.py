from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Vista para iniciar sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('/')  # Redirigir a la página principal o a la que prefieras
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'autenticacion/login.html')

# Vista para registrar usuarios
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está en uso.')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')

    return render(request, 'autenticacion/register.html')

# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('listbook')
