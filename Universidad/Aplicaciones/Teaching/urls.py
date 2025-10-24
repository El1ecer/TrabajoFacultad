from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexTeacher),
    path('nuevoDocente/', views.nuevoDocente),
    path('guardarDocente/', views.guardarDocente),
    path('editarDocente/<int:id>/', views.editarDocente),
    path('guardarEdicionDocente/', views.guardarEdicionDocente),
    path('eliminarDocente/<int:id>/', views.eliminarDocente),
]
