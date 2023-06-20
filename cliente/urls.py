from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('portfolio-details/<id>/',views.portfolio_details,name='portfolio-details'),
]