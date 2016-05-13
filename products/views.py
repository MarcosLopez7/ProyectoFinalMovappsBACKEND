from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from .models import *
from serializers import UsuarioSerializer
# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    usuarios = Usuario.objects.all()
    serializer_class = UsuarioSerializer

@csrf_protect
def login(request):

    if request.method == 'POST':

        return HttpResponse({'email': request.POST.get('email', ''),
                             'password': request.POST.get('password', '')})

    else:
        return HttpResponse("Probando")
