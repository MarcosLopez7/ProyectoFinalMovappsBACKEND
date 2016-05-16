from django.shortcuts import HttpResponse
from django.utils import encoding
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.filters import (
    SearchFilter
)

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
    UsuarioDetailSerializer,
    UsuarioListSerializer,
    UsuarioLoginSerializer,
    FleteListSerializer,
    CategoriaListSerializer,
    UpdateAprobacionSerializer,
    UpdateVentaSerializer,
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

class UsuarioUpdateAPIView(UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer

class UsuarioDestroyAPIView(DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer

class UsuarioDetailAPIView(RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer

class ProductosNotApprovedAPIView(ListAPIView):
    queryset = Producto.objects.filter(aprobado=False)
    serializer_class = ProductoDetailSerializer

class ProductosByCategoriaAPIView(ListAPIView):
    serializer_class = ProductoDetailSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list =  Producto.objects.filter(vendido=False, aprobado=True)
        query = self.request.GET.get("categoria")
        if query:
            queryset_list = queryset_list.filter(
                Q(categoria__id=query)
            )
        return queryset_list

class ProductoByTextAPIView(ListAPIView):
    serializer_class = ProductoDetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre', 'descripcion']
    #no joda
    def get_queryset(self, *args, **kwargs):
        queryset_list = Producto.objects.filter(vendido=False, aprobado=True)
        query = self.request.GET.get("text")
        if query:
            queryset_list = queryset_list.filter(
                Q(nombre__icontains=query)|
                Q(descripcion__icontains=query)
            )
        return queryset_list

class ProductoByUserVendidoAPIView(ListAPIView):
    serializer_class = ProductoDetailSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Producto.objects.filter(vendido=True)
        query = self.request.GET.get("owner")
        if query:
            queryset_list = queryset_list.filter(
                Q(usuario__id=query)
            )
        return queryset_list

class ProductoByUserCompradoAPIView(ListAPIView):
    serializer_class = ProductoDetailSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Producto.objects.filter(vendido=True)
        query = self.request.GET.get("client")
        if query:
            queryset_list = queryset_list.filter(
                Q(compra__cliente=query)
            )
        return queryset_list

class UsuarioByNameAPIView(ListAPIView):
    serializer_class = UsuarioDetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre', 'apellidos', 'email']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Usuario.objects.all()
        query = self.request.GET.get("text")
        if query:
            queryset_list = queryset_list.filter(
                Q(nombre__icontains=query)|
                Q(apellidos__icontains=query)|
                Q(email__icontains=query)
            )
        return queryset_list

class UsuarioLoginAPIView(APIView):

    def post(self, request, format=None):
        queryset_list = Usuario.objects.all()
        serializer = UsuarioLoginSerializer(data=request.data)
        filter_backends = [SearchFilter]
        search_fields = ['email', 'contrasena']

        if serializer.is_valid():
            email = self.request.data['email']
            contrasena = self.request.data['contrasena']
            usuario = Usuario.objects.filter(email=email, contrasena=contrasena)
            print(usuario[0])
            if len(usuario) != 0:
                serializer = UsuarioDetailSerializer(usuario[0])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("invalid", status=status.HTTP_201_CREATED)
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

class CategoriaListAPIView(ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaListSerializer

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

class FleteListAPIView(ListAPIView):
    queryset = Flete.objects.all()
    serializer_class = FleteListSerializer

class UpdateProductoAprobacionAPIVIew(UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = UpdateAprobacionSerializer
    lookup_field = 'pk'

class UpdateProductoVentaAPIVIew(UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = UpdateVentaSerializer
    lookup_field = 'pk'





