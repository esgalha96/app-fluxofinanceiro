from django.shortcuts import redirect, render
import os
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse
import pandas as pd
from django.contrib.auth.decorators import login_required
from acesso.models import Usuario
from page.models import Categoria, Entradas, Saidas

@login_required
def integracao(request):
    return render(request, "integracao.html")

@login_required
def download_file(request):
    # caminho do arquivo
    file_path = os.path.join(settings.STATIC_ROOT, 'xlsx/base.xlsx')

    # abra o arquivo
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="base.xlsx"'
        return response

@login_required
def integracao_process(request):
    if request.method == "GET":
        return redirect(reverse('homepage'))
    elif request.method == "POST":

        try:
            usuario = request.user
            arquivo = request.FILES['arquivo']
            df_base = pd.read_excel(arquivo)

            if len(df_base["Data (dd/MM/aaaa)"]) >= 5000:
                return HttpResponse("Arquivo com mais de 5000 linhas!")
            
            for i, row in df_base.iterrows():
                input_data = row["Data (dd/MM/aaaa)"]
                input_tipo = row["Tipo (Entrada ou Saída)"]
                input_valor = row["Valor (R$)"]
                input_categoria = row["Categoria"]
                input_descricao = row["Descrição"]

                categoria = Categoria.objects.filter(categoria=input_categoria, usuario=usuario).first()

                if not categoria:
                    categoria = Categoria.objects.create(usuario=usuario, categoria=input_categoria)
                
                if input_tipo == "Saída":
                    saida = Saidas.objects.create(
                        usuario=usuario,
                        valor=float(str(input_valor).replace(".","").replace(",",".")),
                        data=input_data,
                        descricao=input_descricao,
                        categoria=categoria
                    )
                    saida.save()
                elif input_tipo == "Entrada":
                    entrada = Entradas.objects.create(
                        usuario=usuario,
                        valor=float(str(input_valor).replace(".","").replace(",",".")),
                        data=input_data,
                        descricao=input_descricao,
                        categoria=categoria
                    )
                    entrada.save()

        except Exception as e:
            print("Erro: " + str(e))
            return HttpResponse("Erro processamento")

        return redirect(reverse('homepage'))