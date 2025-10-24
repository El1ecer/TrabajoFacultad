from django.db import models
from Aplicaciones.Career.models import Careers

class Teachings(models.Model):
    id = models.AutoField(primary_key=True)

   
    carrera = models.ForeignKey( Careers, on_delete=models.CASCADE )

    
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=160, null=True, blank=True)

    
    logo = models.FileField(
        upload_to='cargos',  
        null=True,
        blank=True
    )
    pdf = models.FileField(
        upload_to='pdfs',      
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.carrera.name_career}"

