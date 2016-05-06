from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Django REST API")