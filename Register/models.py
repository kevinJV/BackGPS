from django.db import models
from Profile.models import Profile
import datetime

# Create your models here.

class Dispositivo(models.Model):
        
    Nombre = models.CharField(max_length = 50, null = False)
    Marca = models.CharField(max_length = 50, null = False)
    Modelo = models.CharField(max_length = 50, null = True)
    Imei = models.CharField(max_length = 50, null = False, default = "")   


 