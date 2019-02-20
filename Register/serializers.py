from rest_framework import serializers

from .models import Dispositivo

class DispositivoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dispositivo
        fields = ('id', 'Nombre', 'Marca', 'Modelo', 'Imei')  

# class RegisterSerializer(serializers.ModelSerializer):
#     #Dispositivo = DispositivoSerializer(read_only=True)    
    
#     class Meta:
#         model = Register
#         fields = ('id', 'Profile', 'Dispositivo')

      