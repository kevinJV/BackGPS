from django.db import models
from Unidades.models import Unidades
import datetime

# Create your models here.

class Gps(models.Model):
        
    Latitud = models.CharField(max_length = 255, null = False)
    Longitud = models.CharField(max_length = 255, null = False)
    Fecha = models.DateField(max_length = 10, null = True)
    Hora = models.TimeField(max_length =50, null = True)
    Imei = models.CharField(max_length = 50, null = False)
    Unidad = models.ForeignKey(Unidades, on_delete = models.CASCADE)  

    #class Meta:
    #    db_table = "Gps"