from django.conf.urls import url

from .views import (
    UsuarioCreateAPIView,
    CategoriaCreateAPIView,
    ProductoCreateAPIView,
    CompraCreateAPIView,
    ProductoUpdateAPIView,
    ProductoDetailAPIView,
    ProductoDestroyAPIView,
    DireccionCreateAPIView,
    CategoriaUpdateAPIView,
    CategoriaDestroyAPIView,
    CompraDetailAPIView,
    CompraDestroyAPIView,
    CompraUpdateAPIView,
    DireccionDetailAPIView,
    DireccionUpdateAPIView,
    DireccionDestroyAPIView,
    UsuarioLoginAPIView,
)


urlpatterns = [
    url(r'^login/$', UsuarioLoginAPIView.as_view(), name='login'),
    url(r'^create/$', UsuarioCreateAPIView.as_view(), name='create'),
    url(r'^createcategoria/$', CategoriaCreateAPIView.as_view(), name='createcategoria'),
    url(r'^createproduct/$', ProductoCreateAPIView.as_view(), name='createproduct'),
    url(r'^createcompra/$', CompraCreateAPIView.as_view(), name='createcompra'),
    url(r'edit/(?P<pk>\d+)/$', ProductoUpdateAPIView.as_view(), name='updateproducto'),
    url(r'delete/(?P<pk>\d+)/$', ProductoDestroyAPIView.as_view(), name='deleteproducto'),
    url(r'^createdireccion/$', DireccionCreateAPIView.as_view(), name="createdireccion"),
    url(r'^updatecategoria/(?P<pk>\d+)/$', CategoriaUpdateAPIView.as_view(), name="updatecategoria"),
    url(r'^deletecategoria/(?P<pk>\d+)/$', CategoriaDestroyAPIView.as_view(), name="deletecategoria"),
    url(r'^compra/(?P<pk>\d+)/$', CompraDetailAPIView.as_view(), name="compra"),
    url(r'^updatecompra/(?P<pk>\d+)/$', CompraUpdateAPIView.as_view(), name="updatecompra"),
    url(r'^deletecompra/(?P<pk>\d+)/$', CompraDestroyAPIView.as_view(), name="deletecompra"),
    url(r'^direccion/(?P<pk>\d+)/$', DireccionDetailAPIView.as_view(), name="direccion"),
    url(r'^updatedireccion/(?P<pk>\d+)/$', DireccionUpdateAPIView.as_view(), name="updatedireccion"),
    url(r'^deletedireccion/(?P<pk>\d+)/$', DireccionDestroyAPIView.as_view(), name="deletedireccion"),
    url(r'(?P<pk>\d+)/$', ProductoDetailAPIView.as_view(), name='producto'),
]