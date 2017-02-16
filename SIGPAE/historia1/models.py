from __future__ import unicode_literals

from django.db import models
from django.core.validators import *
from datetime import date

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class Transcripcion(models.Model):
    EM = 'EM'
    AJ = 'AJ'
    SD = 'SD'
    PERIODOS = (
      (EM, 'Enero - Marzo'),
      (AJ, 'Abril - Julio'),
      (SD, 'Septiembre - Diciembre'),
    )
    periodo = models.CharField(
      max_length = 2,
      choices = PERIODOS,
      default = EM,
    )
    year = models.IntegerField(default=date.today().year,validators=[MaxValueValidator(date.today().year), MinValueValidator(1956,message="Año no puede ser menor a 1956")])