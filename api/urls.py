from django.urls import path, reverse_lazy, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt import views as jwt_views
from .views import (LoginView, OauthDeclaraciones, estadisticasGraficasView, estadisticasView,
                    declaracionesJsonView, consultaEstatusTaskJSONDeclaracion, eliminarProcesoJSON, ActualizarUsuarioInfoPerFija)

urlpatterns = [
    path("iniciar_sesion/", csrf_exempt(OauthDeclaraciones.as_view())),
    path("v2/declaraciones/", csrf_exempt(OauthDeclaraciones.as_view())),
    path("token/", LoginView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("estadisticas/", csrf_exempt(estadisticasView.as_view())),
    path("estadisticas-graficas/", estadisticasGraficasView, name='estadisticas-graficas'),
    path("actualizar_usuario_info/", csrf_exempt(ActualizarUsuarioInfoPerFija.as_view()), name='actualizar_usuario_info'),
    path("declaraciones-json/", declaracionesJsonView, name='declaraciones-json'),
    re_path(r'^estatus_declaraciones_json/$', consultaEstatusTaskJSONDeclaracion, name='estatus_declaraciones_json'),
    re_path(r'^eliminar_declaraciones_json/$', eliminarProcesoJSON, name='eliminar_declaraciones_json'),

]