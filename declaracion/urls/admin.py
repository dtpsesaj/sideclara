from django.urls import path, re_path

from declaracion.views import (consultarDeclaracionesAjax, consultarDeclarantesAjax, BusquedaDeclarantesFormView, InfoDeclarantesFormView, InfoDeclaracionFormView,
                              BusquedaDeclaracionesFormView, BusquedaUsDecFormView, BusquedaUsuariosFormView, NuevoUsuariosOICFormView,
                              EliminarUsuarioFormView,InfoUsuarioFormView,EditarUsuarioFormView,DescargarReportesView,
                              DeclaracionesGraficas,DeclaracionesGraficasData,RegistroDeclaranteFormView, descargarReporteView,descargarReportesExcel,
                              consultaEstatusTaskPDFReporte, consultaEstatusReporteExcel, eliminarProcesoPDFReporte, eliminarProcesoExcelReporte, cambiarEstatusDatosPublicosDeclaracion, 
                              cambiarEstatusExtemporaneaDeclaracion, consultaDeclaraciones, DescargarReportesView, consultarDeclarantesExcel)
from sitio.views import (consultaEstatusTaskPDFDeclaracion, crearPDFDeclaracion, eliminarProcesoPDF)

urlpatterns = [
     path('busqueda-declarantes', BusquedaDeclarantesFormView.as_view(),
          name='busqueda-declarantes'),
     path('busqueda-declaraciones', BusquedaDeclaracionesFormView.as_view(),
          name='busqueda-declaraciones'),
     path('busqueda-usuarios', BusquedaUsuariosFormView.as_view(),
          name='busqueda-usuarios'),
     path('busqueda-declarantes-declaraciones', BusquedaUsDecFormView.as_view(),
          name='busqueda-declarantes-declaraciones'),
          
     path('info-declarante/<int:pk>/<tipo_registro>/', InfoDeclarantesFormView.as_view(),
          name='info-declarante'),
     path('info-usuario/<int:pk>/', InfoUsuarioFormView.as_view(),
          name='info-usuario'),

     path('reporte/<tipo>', DescargarReportesView.as_view(),
          name='reporte'),

     path('declaraciones-graficas', DeclaracionesGraficas.as_view(),
          name='declaraciones-graficas'),

     path('api-graficas-data', DeclaracionesGraficasData.as_view(),
          name='api-graficas-data'), 

     path('eliminar-usuario/<int:pk>/', EliminarUsuarioFormView.as_view(),
          name='eliminar-usuario'),
     path('editar-usuario/<int:pk>/', EditarUsuarioFormView.as_view(),
          name='editar-usuario'),
     path('nuevo-usuario', NuevoUsuariosOICFormView.as_view(),
          name='nuevo-usuario'),

     path('nuevo-usuario-declarante',RegistroDeclaranteFormView.as_view(),
          name='nuevo-usuario-declarante'),
     path('editar-usuario-declarante/<int:pk>/<tipo_registro>/',RegistroDeclaranteFormView.as_view(),
          name='editar-usuario-declarante'),

     path('info-declaracion/<int:pk>/<tipo>/', InfoDeclaracionFormView.as_view(),
          name='info-declaracion'),
     re_path(r'^reporte/excel/declaraciones/$', descargarReportesExcel, name='descargarReporteExcel'),
     re_path(r'^consultaDeclaraciones/$', consultaDeclaraciones, name='consultaDeclaraciones'),
     re_path(r'^reporte/crear/$', descargarReporteView, name='crear_reporte'),
     re_path(r'^reporte/consultar/$', consultaEstatusTaskPDFReporte, name='consultar_estatus_reporte'),
     re_path(r'^reporte/excel/consultar/$', consultaEstatusReporteExcel, name='consultar_estatus_reporte_excel'),
     re_path(r'^reporte/eliminar/$', eliminarProcesoPDFReporte, name='eliminar_procesos_reporte'),
     re_path(r'^reporte/excel/eliminar/$', eliminarProcesoExcelReporte, name='eliminar_procesos_reporte_excel'),
     re_path(r'^consultar/declaraciones/$', consultarDeclaracionesAjax, name='consultarDeclaracionesAjax'),
     re_path(r'^consultar/declarantes/$', consultarDeclarantesAjax, name='consultarDeclarantesAjax'),
     re_path(r'^consultar/declarantesexel/$', consultarDeclarantesExcel, name='consultarDeclarantesAjaxExcel'),
     re_path(r'^busqueda-declaraciones/crear_pdf_declaracion/$', crearPDFDeclaracion, name='crear_pdf_declaracion'),
     re_path(r'^busqueda-declaraciones/estatus_pdf_declaracion/$', consultaEstatusTaskPDFDeclaracion, name='estatus_pdf_declaracion'),
     re_path(r'^busqueda-declaraciones/eliminar_pdf_declaracion_proceso/$', eliminarProcesoPDF, name='eliminar_pdf_declaracion_proceso'),
     re_path(r'^busqueda-declaraciones/declaracion/cambiar_datos_publicos$', cambiarEstatusDatosPublicosDeclaracion, name='cambiar_datos_publicos'),
     re_path(r'^busqueda-declaraciones/declaracion/cambiar_extemporanea$', cambiarEstatusExtemporaneaDeclaracion, name='cambiar_extemporanea'),
]
