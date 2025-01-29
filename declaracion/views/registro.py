from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View

from declaracion.forms import RegistroForm, CambioEntePublicoForm
from declaracion.models import InfoPersonalFija, InfoPersonalVar, Declaraciones
from declaracion.views.utils import obtiene_avance, obtiene_rfc
from sitio.util import account_activation_token
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from sitio.models import sitio_personalizacion as personalizacion, Valores_SMTP
from .mailto import mail_conf

from declaracion.models.catalogos import (CatPuestos)
from django.http import JsonResponse

import requests
import json


def listaPuestos(request):
    """
    Función que se encarga de filtar los puestos de las areas
    """
    area = request.GET.get('area')
    response = {}
    puestos = CatPuestos.objects.none()
    listaPuestos = []


    if area:
        puestos = CatPuestos.objects.filter(cat_areas=area)#django.db.models.query.QuerySet

    for puesto in puestos:
        varTem = {
            "value":puesto.pk, 
            "text":f'{puesto.cat_areas.codigo} - {puesto.puesto}', #f-Strings: A new and improved way to Format Strings
            "nivel": puesto.codigo
        } 

        listaPuestos.append(varTem)   

    response['Puestos'] = listaPuestos # Agregar listaPuestos[] a una llave.

    return JsonResponse(response)#response es de tipo Diccionario.


class RegistroView(View):
    """
    Class RegistroView vista basada en clases guarda los usuarios de nuevo ingreso
    """
    template_name = 'declaracion/registro.html'
    template_redirect='sitio/login.html'
    form_redirect = None
    is_staff = False
    try:
        cap_webkey =personalizacion.objects.first().google_captcha_sitekey

    except Exception as e:
        cap_webkey =''



    def get(self, request, *args, **kwargs):
        """
        Function get muestra formulario de registro y precarga algunos valores
        """
        return redirect(settings.LOGIN_URL+'registro/')


class PerfilView(View):
    """
    Classs PerfilView muestra información resumida del perfil de usuario
    """
    template_name="declaracion/perfil.html"

    @method_decorator(login_required(login_url='/login'))
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        form = CambioEntePublicoForm()
        infopersonalfija = InfoPersonalFija.objects.filter(usuario=request.user).first()
        if infopersonalfija is None:
            declaracion = None
        else:
            try:
                declaracion = Declaraciones.objects.filter(info_personal_fija=infopersonalfija).filter(
                    Q(cat_estatus__isnull=True) | Q(cat_estatus__pk__in=(1, 2, 3))).first()
            except:
                pass

            try:
                declaracion.avance= obtiene_avance(declaracion)[0]
                declaracion.save()
            except Exception as e:
                print(e)

        return render(request, self.template_name, {
            'user':request.user,
            'form':form,
            'infopersonalfija':infopersonalfija,
            'declaracion':declaracion,
            'personalizacion': personalizacion.objects.all()[0],
            "current_url_menu": "inicio"
        })



    @method_decorator(login_required(login_url='/login'))
    def post(selfself,request):
        form = CambioEntePublicoForm(request.POST)
        if form.is_valid():
            InfoPersonalFija.objects.filter(usuario=request.user).update(nombre_ente_publico=form.cleaned_data.get('nombre_ente_publico'))
            return HttpResponse(content="",status=200)
        else:
            return HttpResponse(content="Campo sin llenar",status=500)
