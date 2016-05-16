from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField
from .models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellidos', 'email', 'contrasena', 'telefono', 'foto', 'administrador', 'video')

class UsuarioListSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email', 'contrasena')

class UsuarioDetailSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('pk', 'nombre', 'apellidos', 'email', 'contrasena', 'telefono', 'foto', 'administrador', 'video')

class UsuarioLoginSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email', 'contrasena')

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
        fields = ('pk', 'nombre', 'descripcion', 'precio', 'foto', 'ultima_modificacion', 'aprobado', 'vendido', 'usuario',
                  'categoria')

class CreateProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'foto', 'ultima_modificacion', 'aprobado', 'vendido', 'usuario',
                  'categoria')

class ProductoDetailSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ('pk', 'nombre', 'descripcion', 'precio', 'foto', 'ultima_modificacion', 'aprobado', 'vendido',
                  'usuario', 'categoria')

class CreateCompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ('producto', 'cliente', 'entregado', 'precio_total', 'metodo_pago', 'coordenadasX', 'coordenadasY',
                  'flete')

class CreateDireccionSerializer(ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('ciudad', 'municipio', 'codigo_postal', 'direccion', 'colonia', 'usuario')

class CategoriaDetailSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('pk', 'nombre', 'descripcion')

class CategoriaListSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('pk', 'nombre', 'descripcion')

class CompraDetailSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ('pk', 'producto', 'cliente', 'entregado', 'precio_total', 'metodo_pago', 'coordenadasX', 'coordenadasY',
                  'flete')

class DireccionDetailSerializer(ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('pk', 'ciudad', 'municipio', 'codigo_postal', 'direccion', 'colonia', 'usuario')

class FleteListSerializer():
    class Meta:
        model = Flete
        fields = ('pk', 'nombre', 'precio')

class UpdateAprobacionSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ('ultima_modificacion', 'aprobado')