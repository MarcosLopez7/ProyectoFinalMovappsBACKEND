from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from .models import *
from .serializers import (
    UsuarioSerializer,
    CreateUsuarioSerializer,
    CreateCategoriaSerializer,
    CreateProductoSerializer,
    ProductoSerializer
)

from rest_framework.generics import (
    CreateAPIView
)
# Create your views here.

class UsuarioCreateAPIView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = CreateUsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaCreateAPIView(CreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CreateCategoriaSerializer

class ProductoCreateAPIView(CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = CreateProductoSerializer

@csrf_protect
def login(request):

    if request.method == 'POST':

        return HttpResponse({'email': request.POST.get('email', ''),
                             'password': request.POST.get('password', '')})

    else:
        return HttpResponse("Probando")

