from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('sitio.urls')),
    path('admin/', admin.site.urls),
    path('declaracion/', include('declaracion.urls')),
    path('api/', include('api.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),  
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),  
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),  
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete')
]


admin.site.site_header = 'Administración de Declaraciones'
admin.site.site_title = 'Administración de Declaraciones'
admin.site.index_title =  'Bienvenido a la administración del sistema'
