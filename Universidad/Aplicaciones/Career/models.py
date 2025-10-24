from django.db import models
from Aplicaciones.Faculty.models import Facultys

class Careers(models.Model):
    id = models.AutoField(primary_key=True)

    facultad = models.ForeignKey( Facultys, on_delete = models.CASCADE )

    name_career = models.CharField(max_length=150)
    directory_car = models.CharField(max_length=15, null=True, blank=True)
    duration_years = models.IntegerField(null=True, blank=True)   
    phone_car = models.CharField(max_length=15, null=True, blank=True)
    email_car = models.CharField(max_length=50, null=True, blank=True)

    # Archivos (como en tu ejemplo)
    logo = models.FileField(
        upload_to='cargos',  
        null=True,
        blank=True
    )

    def __str__(self):
        # Muestra el nombre de la carrera y la facultad
        return f"{self.name_career} - {self.facultad.nombre_facultad}"
