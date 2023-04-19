from django.urls import path
from . import views

urlpatterns = [
    path("report_saidas/", views.report_saidas, name="report_saidas"),
    path("report_entradas/", views.report_entradas, name="report_entradas"),
    
]