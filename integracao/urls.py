from django.urls import path
from . import views

urlpatterns = [
    path('', views.integracao, name='integracao'),
    path('download_file/', views.download_file, name='download_file'),
    path('integracao_process/', views.integracao_process, name="integracao_process"),

]