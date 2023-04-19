import decimal
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from acesso.models import Usuario
from .models import Categoria, Saidas, Entradas
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from datetime import datetime as dt
import numpy as np
from .forms import EntradasForm, SaidasForm, CategoriasForm

def homepage(request):
    
    return render(request, 'homepage.html', {})

@login_required
def perfil(request):
    
    usuario_logado = request.user
    msg_success = ""

    if request.POST:

        usuario_att = Usuario.objects.filter(id=request.user.id).first()
        
        usuario_att.cpf = request.POST.get('cpf')
        usuario_att.email = request.POST.get('email')
        usuario_att.cep = request.POST.get('cep')
        usuario_att.save()

        if usuario_att:
            msg_success = "Cadastro atualizado com sucesso!"
            usuario_logado = usuario_att
        
 
    context={
        'usuario_logado':usuario_logado,
        'msg_success': msg_success,
    }

    return render(request, 'perfil.html', context)

@login_required
def categorias(request):
 
    usuario_logado = request.user
    categorias_usuario = Categoria.objects.filter(usuario=usuario_logado)

    context={
        "usuario_logado": usuario_logado,
        "categorias_usuario": categorias_usuario
    }

    return render(request, 'categorias.html', context)

@login_required
def categorias_delete(request, id):
 
    categoria_usuario = Categoria.objects.filter(id=id).first()

    if categoria_usuario:
        categoria_usuario.delete()

    return redirect('categorias')

def categorias_add(request):

    if request.method == "POST":
        form = CategoriasForm(data = request.POST, id_usuario=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = CategoriasForm(id_usuario=request.user.id)

    context = {
        'form': form,
    }

    return render(request, 'categorias_add.html', context)

@login_required
def entradas(request):
 
    usuario_logado = request.user
    entradas_usuario = Entradas.objects.filter(usuario=usuario_logado)[:15]

    context={
        "usuario_logado": usuario_logado,
        "entradas_usuario": entradas_usuario
    }

    return render(request, 'entradas.html', context)

@login_required
def entradas_edit(request, id):
 
    usuario_logado = request.user
    form = EntradasForm(id_usuario=request.user.id)

    if request.method == "GET":
        
        entrada_usuario = Entradas.objects.filter(id=id).first()

        initial = {
            'id': id,
            'valor': entrada_usuario.valor,
            'data': entrada_usuario.data,
            'categoria': entrada_usuario.categoria,
            'descricao': entrada_usuario.descricao
        }

        form = EntradasForm(initial = initial, id_usuario = request.user.id)

    elif request.POST:

        id_entrada = request.POST.get('id_entrada')
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')

        ano = int(data.split('/')[2])
        mes = int(data.split('/')[1])
        dia = int(data.split('/')[0])

        entrada = Entradas.objects.filter(id=id_entrada).first()
        entrada.valor = valor
        entrada.data = timezone.datetime(ano,mes,dia)
        entrada.categoria = Categoria.objects.filter(id=categoria).first()
        entrada.descricao = descricao

        entrada.save()

        return redirect('entradas')

    context={
        'id_entrada': id,
        "usuario_logado": usuario_logado,
        "form": form,
    }

    return render(request, 'entradas_edit.html', context)

@login_required
def entradas_delete(request, id):
 
    entrada_usuario = Entradas.objects.filter(id=id).first()

    if entrada_usuario:
        entrada_usuario.delete()

    return redirect('entradas')

def entradas_add(request):

    if request.method == "POST":
        form = EntradasForm(data = request.POST, id_usuario=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('entradas')
    else:
        form = EntradasForm(id_usuario=request.user.id)

    context = {
        'form': form,
    }

    return render(request, 'entradas_add.html', context)

@login_required
def saidas(request):

    usuario_logado = request.user
    saidas_usuario = Saidas.objects.filter(usuario=usuario_logado)[:15]

    context={
        "usuario_logado": usuario_logado,
        "saidas_usuario": saidas_usuario
    }

    return render(request, 'saidas.html', context)

@login_required
def saidas_edit(request, id):
 
    usuario_logado = request.user
    form = SaidasForm(id_usuario=request.user.id)

    if request.method == "GET":
        
        saida_usuario = Saidas.objects.filter(id=id).first()

        initial = {
            'id': id,
            'valor': saida_usuario.valor,
            'data': saida_usuario.data,
            'categoria': saida_usuario.categoria,
            'descricao': saida_usuario.descricao
        }

        form = SaidasForm(initial = initial, id_usuario = request.user.id)

    elif request.POST:

        id_saida = request.POST.get('id_saida')
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')

        ano = int(data.split('/')[2])
        mes = int(data.split('/')[1])
        dia = int(data.split('/')[0])

        saida = Saidas.objects.filter(id=id_saida).first()
        saida.valor = valor
        saida.data = timezone.datetime(ano,mes,dia)
        saida.categoria = Categoria.objects.filter(id=categoria).first()
        saida.descricao = descricao

        saida.save()

        return redirect('saidas')

    context={
        'id_saida': id,
        "usuario_logado": usuario_logado,
        "form": form,
    }

    return render(request, 'saidas_edit.html', context)

@login_required
def saidas_delete(request, id):
 
    saida_usuario = Saidas.objects.filter(id=id).first()

    if saida_usuario:
        saida_usuario.delete()

    return redirect('saidas')

def saidas_add(request):

    if request.method == "POST":
        form = SaidasForm(data = request.POST, id_usuario=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('saidas')
    else:
        form = SaidasForm(id_usuario=request.user.id)

    context = {
        'form': form,
    }

    return render(request, 'saidas_add.html', context)

@login_required
def dashboard(request):

    usuario_logado = request.user

    context={
        "usuario_logado": usuario_logado,
        
    }

    return render(request, 'dashboard.html', context)

def dados_dashboard_saidas(request):

    usuario_logado = request.user
    saidas_usuario = Saidas.objects.filter(usuario=usuario_logado)

    ano = timezone.now().year
    mes = timezone.now().month

    labels = []
    
    for i in range(6):
        labels.append(str(mes)+"/"+str(ano))
        mes -= 1
        if mes == 0:
            ano -= 1
            mes = 12
    labels.reverse()

    valores = []
    soma_por_mes = saidas_usuario.annotate(mes=TruncMonth('data')).values('mes').annotate(soma=Sum('valor'))

    for mes_ano in labels:
        mes = int(str(mes_ano).split('/')[0])
        ano = int(str(mes_ano).split('/')[1])
        
        try:
            query = soma_por_mes.get(mes=dt(ano, mes, 1))
            valores.append(query['soma'])
        except:
            valores.append(0)
   
    dados = {
        'labels': labels,
        'valores': valores
    }
    return JsonResponse(dados)

def dados_dashboard_entradas(request):

    usuario_logado = request.user
    entradas_usuario = Entradas.objects.filter(usuario=usuario_logado)

    ano = timezone.now().year
    mes = timezone.now().month

    labels = []
    
    for i in range(6):
        labels.append(str(mes)+"/"+str(ano))
        mes -= 1
        if mes == 0:
            ano -= 1
            mes = 12
    labels.reverse()

    valores = []
    soma_por_mes = entradas_usuario.annotate(mes=TruncMonth('data')).values('mes').annotate(soma=Sum('valor'))

    for mes_ano in labels:
        mes = int(str(mes_ano).split('/')[0])
        ano = int(str(mes_ano).split('/')[1])
        
        try:
            query = soma_por_mes.get(mes=dt(ano, mes, 1))
            valores.append(query['soma'])
        except:
            valores.append(0)
   
    dados = {
        'labels': labels,
        'valores': valores
    }
    return JsonResponse(dados)

def get_saldo_anterior(request, data):

    #data = mm/YYYY
    mes = int(data.split('/')[0])
    ano = int(data.split('/')[1])

    all_entradas = Entradas.objects.filter(usuario=request.user, data__lt=timezone.datetime(ano, mes, 1))
    all_saidas = Saidas.objects.filter(usuario=request.user, data__lt=timezone.datetime(ano, mes, 1))

    all_entradas = all_entradas.order_by('data').aggregate(Sum('valor'))['valor__sum']
    all_saidas = all_saidas.order_by('data').aggregate(Sum('valor'))['valor__sum']

    if all_entradas == None:
        all_entradas = decimal.Decimal(0)
    if all_saidas == None:
        all_saidas = decimal.Decimal(0)
    
    return all_entradas - all_saidas

def dados_dashboard_fluxo_caixa(request):

    usuario_logado = request.user
    entradas_usuario = Entradas.objects.filter(usuario=usuario_logado)
    saidas_usuario = Saidas.objects.filter(usuario=usuario_logado)

    ano = timezone.now().year
    mes = timezone.now().month

    labels = []
    
    for i in range(6):
        labels.append(str(mes)+"/"+str(ano))
        mes -= 1
        if mes == 0:
            ano -= 1
            mes = 12
    labels.reverse()

    valores = {'entradas':[], 'saidas':[], 'fluxo':[]}
    soma_por_mes_entradas = entradas_usuario.annotate(mes=TruncMonth('data')).values('mes').annotate(soma=Sum('valor'))
    soma_por_mes_saidas = saidas_usuario.annotate(mes=TruncMonth('data')).values('mes').annotate(soma=Sum('valor'))

    for mes_ano in labels:
        mes = int(str(mes_ano).split('/')[0])
        ano = int(str(mes_ano).split('/')[1])
        
        try:
            query_entradas = soma_por_mes_entradas.get(mes=dt(ano, mes, 1))
            valores['entradas'].append(query_entradas['soma'])
        except:
            valores['entradas'].append(0)

        try:
            query_saidas = soma_por_mes_saidas.get(mes=dt(ano, mes, 1))
            valores['saidas'].append(query_saidas['soma'])
        except:
            valores['saidas'].append(0)

    saldo_anterior = get_saldo_anterior(request, labels[0])

    for i, entrada, saida in zip(range(6), valores['entradas'], valores['saidas']):
        if i == 0:
            valores['fluxo'].append(saldo_anterior + entrada - saida)
        else:
            valores['fluxo'].append(valores['fluxo'][i-1] + entrada - saida)

    dados = {
        'labels': labels,
        'valores': valores
    }
    return JsonResponse(dados)

def dados_dashboard_saidas_categoria(request):

    usuario_logado = request.user
    saidas_usuario = Saidas.objects.filter(usuario=usuario_logado)

    labels = []
    valores = {'saidas':[]}

    queryset = saidas_usuario.values('categoria').annotate(total=Sum('valor'))

    for data in queryset:
        labels.append(Categoria.objects.filter(id=data['categoria']).first().categoria)
        valores['saidas'].append(data['total'])

    dados = {
        'labels': labels,
        'valores': valores
    }
    return JsonResponse(dados)

def dados_dashboard_entradas_categoria(request):

    usuario_logado = request.user
    entradas_usuario = Entradas.objects.filter(usuario=usuario_logado)

    labels = []
    valores = {'entradas':[]}

    queryset = entradas_usuario.values('categoria').annotate(total=Sum('valor'))

    for data in queryset:
        labels.append(Categoria.objects.filter(id=data['categoria']).first().categoria)
        valores['entradas'].append(data['total'])

    dados = {
        'labels': labels,
        'valores': valores
    }
    return JsonResponse(dados)