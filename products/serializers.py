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

class CreateCategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion')

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'foto', 'ultima_modificacion', 'aprobado', 'vendido', 'usuario',
                  'categoria')

class CreateProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'foto', 'ultima_modificacion', 'aprobado', 'vendido', 'usuario',
                  'categoria')

class CreateCompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ('producto', 'cliente', 'entregado', 'precio_total', 'metodo_pago', 'coordenadasX', 'coordenadasY',
                  'flete')