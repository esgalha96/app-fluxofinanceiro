from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('perfil/', views.perfil, name="perfil"),
    path('categorias/', views.categorias, name="categorias"),
    path('categorias/add', views.categorias_add, name="categorias_add"),
    path('categorias/delete/<int:id>/', views.categorias_delete, name="categorias_delete"),
    path('entradas/', views.entradas, name="entradas"),
    path('entradas/add', views.entradas_add, name="entradas_add"),
    path('entradas/edit/<int:id>/', views.entradas_edit, name="entradas_edit"),
    path('entradas/delete/<int:id>/', views.entradas_delete, name="entradas_delete"),
    path('saidas/', views.saidas, name="saidas"),
    path('saidas/add', views.saidas_add, name="saidas_add"),
    path('saidas/edit/<int:id>/', views.saidas_edit, name="saidas_edit"),
    path('saidas/delete/<int:id>/', views.saidas_delete, name="saidas_delete"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dados_dashboard_saidas/', views.dados_dashboard_saidas, name="dados_dashboard_saidas"),
    path('dados_dashboard_entradas/', views.dados_dashboard_entradas, name="dados_dashboard_entradas"),
    path('dados_dashboard_fluxo_caixa/', views.dados_dashboard_fluxo_caixa, name="dados_dashboard_fluxo_caixa"),


]