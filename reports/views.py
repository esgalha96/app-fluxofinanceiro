from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from page.models import Saidas, Entradas, Categoria
from django.shortcuts import render
from reports.base_report import ReportBase, cm

@login_required
def report_saidas(request):
    
    saidas_list = []
    queryset = Saidas.objects.filter(usuario=request.user)

    for saida in queryset:
        saidas_list.append([saida.data.strftime(f'%d/%m/%Y'), saida.categoria.categoria, saida.descricao, saida.valor])

    response = ReportBase(
        request, 
        "Relatório Saídas",
        'staticfiles/logo/logo.png'
        ).report_table(
        ["Data", "Categoria", "Desrição", "Valor"],
        saidas_list,
        [3*cm, 5*cm, 7*cm, 3*cm]
        )
    
    return response


@login_required
def report_entradas(request):
    
    entradas_list = []
    queryset = Entradas.objects.filter(usuario=request.user)

    for saida in queryset:
        entradas_list.append([saida.data.strftime(f'%d/%m/%Y'), saida.categoria.categoria, saida.descricao, saida.valor])

    response = ReportBase(
        request, 
        "Relatório Entradas",
        'staticfiles/logo/logo.png'
        ).report_table(
        ["Data", "Categoria", "Desrição", "Valor"],
        entradas_list,
        [3*cm, 5*cm, 7*cm, 3*cm]
        )
    
    return response

