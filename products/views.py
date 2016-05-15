from django.shortcuts import HttpResponse
from django.utils import encoding
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .models import *
from .serializers import (
    UsuarioSerializer,
    CreateUsuarioSerializer,
    CreateCategoriaSerializer,
    CreateProductoSerializer,
    ProductoSerializer,
    CreateCompraSerializer,
    ProductoDetailSerializer,
    CreateDireccionSerializer,
    CategoriaDetailSerializer,
    CompraDetailSerializer,
    DireccionDetailSerializer,
    UsuarioListSerializer,
    UsuarioLoginSerializer,
)
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView

from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
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

class UsuarioLoginAPIView(APIView):

    def post(self, request, format=None):
        serializer = UsuarioLoginAPIView(data=request.data)
        if serializer.is_valid():
            return Response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class ProductoDestroyAPIView(DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoDetailSerializer
    lookup_field = 'pk'

class CompraCreateAPIView(CreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CreateCompraSerializer

class DireccionCreateAPIView(CreateAPIView):
    queryset = Direccion.objects.all()
    serializer_class = CreateDireccionSerializer

class CategoriaUpdateAPIView(UpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaDetailSerializer
    lookup_field = 'pk'

class CategoriaDestroyAPIView(DestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaDetailSerializer
    lookup_field = 'pk'

class CompraDetailAPIView(RetrieveAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraDetailSerializer
    lookup_field = 'pk'

class CompraUpdateAPIView(UpdateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraDetailSerializer
    lookup_field = 'pk'

class CompraDestroyAPIView(DestroyAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraDetailSerializer
    lookup_field = 'pk'

class DireccionDetailAPIView(RetrieveAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionDetailSerializer
    lookup_field = 'pk'

class DireccionUpdateAPIView(UpdateAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionDetailSerializer
    lookup_field = 'pk'

class DireccionDestroyAPIView(DestroyAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionDetailSerializer
    lookup_field = 'pk'
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

