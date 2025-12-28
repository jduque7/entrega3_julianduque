from django.urls import path
from .views import home, agregar_categoria, agregar_material, agregar_joya, buscar

urlpatterns = [
    path('', home, name='home'),
    path('agregar_categoria/', agregar_categoria, name='agregar_categoria'),
    path('agregar_material/', agregar_material, name='agregar_material'),
    path('agregar_joya/', agregar_joya, name='agregar_joya'),
    path('buscar/', buscar, name='buscar'),
]