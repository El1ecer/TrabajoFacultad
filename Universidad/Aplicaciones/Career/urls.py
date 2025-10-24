from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio2, name='inicioCareer'),
    path('nuevaCarrera/', views.nuevaCarrera, name='nuevaCarrera'),
    path('guardarCarrera/', views.GuardarCarrera, name='guardarCarrera'),
    path('editarCarrera/<int:id>/', views.editarCarrera, name='editarCarrera'),
    path('guardarEdicionCarrera/', views.GuardarEdicionCarrera, name='guardarEdicionCarrera'),
    path('eliminarCarrera/<int:id>/', views.EliminarCarrera, name='eliminarCarrera'),
]
