from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellidos', 'email', 'contrasena', 'telefono', 'foto', 'administrador', 'video')

class CreateUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellidos', 'email', 'contrasena', 'telefono', 'foto', 'administrador', 'video')