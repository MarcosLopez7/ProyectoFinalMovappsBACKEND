from django.conf.urls import url

from .views import (
    UsuarioCreateAPIView,
    CategoriaCreateAPIView,
    ProductoCreateAPIView
)


urlpatterns = [
    url(r'^create/$', UsuarioCreateAPIView.as_view(), name='create'),
    url(r'^createcategoria/$', CategoriaCreateAPIView.as_view(), name='createcategoria'),
    url(r'^createproduct/$', ProductoCreateAPIView.as_view(), name='createproduct'),
]