# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas...
    path('', views.input_book, name='inputbook'),
]