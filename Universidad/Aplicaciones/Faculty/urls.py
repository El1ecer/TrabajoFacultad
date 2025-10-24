from django.urls import path
from. import views

urlpatterns = [
    path('', views.inicio1, name='inicioFacultad'),
    path('nuevaFacultad/', views.nuevaFacultad, name='nuevaFacultad'),
    path('guardarFacultad/', views.GuardarFacultad, name='guardarFacultad'),
    path('editarFacultad/<int:id>/', views.editarFacultad, name='editarFacultad'),
    path('guardarEdicionFacultad/', views.GuardarEdicionFacultad, name='guardarEdicionFacultad'),
    path('eliminarFacultad/<int:id>/', views.EliminarFacultad, name='eliminarFacultad'),
]