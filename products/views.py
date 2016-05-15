from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from .models import *
from .serializers import (
    UsuarioSerializer,
    CreateUsuarioSerializer,
    CreateCategoriaSerializer,
    CreateProductoSerializer,
    ProductoSerializer,
    CreateCompraSerializer,
    ProductoDetailSerializer,
    UsuarioLoginSerializer
)
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView

from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
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

class ProductoUpdateAPIView(UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoDetailSerializer
    lookup_field = 'pk'

class ProductoDetailAPIView(RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoDetailSerializer
    lookup_field = 'pk'

class CompraCreateAPIView(CreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CreateCompraSerializer
"""
class UsuarioLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UsuarioLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UsuarioLoginSerializer(data=data)
"""
@csrf_protect
def login(request):

    if request.method == 'POST':

        return HttpResponse({'email': request.POST.get('email', ''),
                             'password': request.POST.get('password', '')})

    else:
        return HttpResponse("Probando")

