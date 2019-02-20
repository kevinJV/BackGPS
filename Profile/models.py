from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    
    User = models.OneToOneField(User, on_delete=models.CASCADE)    
    Address = models.CharField(max_length = 255, null = False)
    Phone = models.CharField(max_length = 10, null = False)
    Email = models.CharField(max_length =50, null = False)
    Edad = models.IntegerField(null = False)
