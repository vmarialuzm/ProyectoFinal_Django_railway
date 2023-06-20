from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autenticacion.urls')),
    path('', include('cliente.urls')),
    path('formulario/', include('formulario.urls')),
]
