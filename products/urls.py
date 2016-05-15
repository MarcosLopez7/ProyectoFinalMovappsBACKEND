from django.conf.urls import url

from .views import (
    UsuarioCreateAPIView,
    CategoriaCreateAPIView,
    ProductoCreateAPIView,
    CompraCreateAPIView,
    ProductoUpdateAPIView,
    ProductoDetailAPIView,
    ProductoDestroyAPIView
)


urlpatterns = [
    url(r'^create/$', UsuarioCreateAPIView.as_view(), name='create'),
    url(r'^createcategoria/$', CategoriaCreateAPIView.as_view(), name='createcategoria'),
    url(r'^createproduct/$', ProductoCreateAPIView.as_view(), name='createproduct'),
    url(r'^createcompra/$', CompraCreateAPIView.as_view(), name='createcompra'),
    url(r'edit/(?P<pk>\d+)/$', ProductoUpdateAPIView.as_view(), name='updateproducto'),
    url(r'(?P<pk>\d+)/$', ProductoDetailAPIView.as_view(), name='producto'),
    url(r'delete/(?P<pk>\d+)/$', ProductoDestroyAPIView.as_view(), name='destroyproducto'),
]