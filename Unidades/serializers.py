from rest_framework import serializers

from .models import Unidades

class UnidadesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Unidades
        fields = ('id', 'Placa', 'User', 'Modelo', 'Imei')