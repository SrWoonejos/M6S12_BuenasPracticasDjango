# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas...
    path('inputbook/', views.input_book, name='inputbook'),
    path('', views.list_books, name='listbook'),
]