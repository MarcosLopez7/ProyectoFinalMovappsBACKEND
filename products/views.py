from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def login(request):

    if request.method == 'POST':

        return HttpResponse({'email': request.POST.get('email', ''),
                             'password': request.POST.get('password', '')})

    else:
        return HttpResponse("Probando")