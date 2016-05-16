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
    UsuarioDestroyAPIView,
    UsuarioUpdateAPIView,
    UsuarioDetailAPIView,
    ProductosNotApprovedAPIView,
    FleteListAPIView,
    CategoriaListAPIView,
    ProductosByCategoriaAPIView
)


urlpatterns = [
    url(r'^login/$', UsuarioLoginAPIView.as_view(), name='login'),
    url(r'^usuario/(?P<pk>\d+)/$', UsuarioDetailAPIView.as_view(), name='usuario'),
    url(r'^updateusuario/(?P<pk>\d+)/$', UsuarioUpdateAPIView.as_view(), name='updateusuario'),
    url(r'^destroyusuario/(?P<pk>\d+)/$', UsuarioDestroyAPIView.as_view(), name='destroyusuario'),
    url(r'^categorias/$', CategoriaListAPIView.as_view(), name="categorias"),
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
    url(r'^productosnotapproved/$', ProductosNotApprovedAPIView.as_view(), name='productosnotapproved'),
    url(r'^fletes/$', FleteListAPIView.as_view(), name='flete'),
    url(r'^productobycategoria/$', ProductosByCategoriaAPIView.as_view(), name="pbyc"),
    url(r'(?P<pk>\d+)/$', ProductoDetailAPIView.as_view(), name='producto'),
]