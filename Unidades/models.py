from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Unidades(models.Model):
        
    Placa = models.CharField(max_length = 100, null = False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)        
    Modelo = models.CharField(max_length = 50, null = False)
    Imei = models.CharField(max_length = 50, null = False)
    