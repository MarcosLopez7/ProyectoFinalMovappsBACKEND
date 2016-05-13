from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellidos', 'email', 'contrasena', 'telefono', 'foto', 'administrador', 'video')