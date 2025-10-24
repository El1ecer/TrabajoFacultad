from django.db import models

# Create your models here.

from django.db import models

class Facultys(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_facultad = models.CharField(max_length=100)
    acronym_fac = models.CharField(max_length=15, null=True, blank=True)
    dean_name_fac = models.CharField(max_length=150, null=True, blank=True)
    phone_fac = models.CharField(max_length=15, null=True, blank=True)
    email_fac = models.CharField(max_length=50, null=True, blank=True)

    logo_fac = models.FileField(
        upload_to='cargos',   
        null=True,
        blank=True
    )

    year_fundation_fac = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_facultad} ({self.acronym_fac})"

