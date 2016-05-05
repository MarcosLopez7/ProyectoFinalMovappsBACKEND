from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Direccion)
admin.site.register(Producto)
admin.site.register(Flete)
admin.site.register(Compra)