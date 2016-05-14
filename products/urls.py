from django.conf.urls import url

from .views import (
    UsuarioCreateAPIView
)


urlpatterns = [
    url(r'^create/$', UsuarioCreateAPIView.as_view(), name='create'),
]