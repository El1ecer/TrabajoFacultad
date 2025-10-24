from django.urls import path
from . import views

urlpatterns = [
    path('nuevoDocente', views.nuevoDocente),
    path('guardarDocente', views.guardarDocente),
    path('editarDocente/<id>', views.editarDocente),
    path('guardarEdicionDocente', views.guardarEdicionDocente),
    path('eliminarDocente/<id>', views.eliminarDocente),
]