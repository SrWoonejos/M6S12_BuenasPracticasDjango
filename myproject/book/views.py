# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book

@login_required  # Restringe el acceso a usuarios autenticados
def input_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        rating = request.POST.get('rating')

        # Validar que la valoración sea numérica y esté en el rango permitido
        try:
            rating = float(rating)
            if 0 <= rating <= 10000:
                # Guardar el libro en la base de datos
                Book.objects.create(title=title, author=author, rating=rating)
                return redirect('inputbook')  # Redirigir tras agregar un libro
            else:
                error = "La valoración debe estar entre 0 y 10000."
        except ValueError:
            error = "La valoración debe ser un número."
    else:
        error = None

    return render(request, 'input_book/input_book.html', {'error': error})
