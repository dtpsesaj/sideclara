from django.urls import path, re_path

from declaracion.views import (RegistroView,PerfilView,listaPuestos)

urlpatterns = [

    path('nuevo', RegistroView.as_view(),
         name='nuevo'),
    path('perfil', PerfilView.as_view(),
         name='perfil'),
    re_path(r'^lista_puestos/$', listaPuestos, name="lista_puestos"),
]
