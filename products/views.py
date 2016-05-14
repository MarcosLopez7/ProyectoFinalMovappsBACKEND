from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from .models import *
from .serializers import UsuarioSerializer, CreateUsuarioSerializer
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



@csrf_protect
def login(request):

    if request.method == 'POST':

        return HttpResponse({'email': request.POST.get('email', ''),
                             'password': request.POST.get('password', '')})

    else:
        return HttpResponse("Probando")

