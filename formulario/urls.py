from django.urls import path
from . import views


urlpatterns = [
    path('crear/',views.CreateProyecto.as_view(), name='crear'),
]