from django.shortcuts import redirect, render
from .models import IncomumAgencia,IncomumAgente,Faturamentosimplificado
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
import time
from django.db.models import Q
from django.core.serializers import serialize
import requests
from django.http import JsonResponse
from django.db import connection
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request,'teste.html')
    if request.method == 'GET':
        return render(request,'index.html')
    elif 1==1:
        login_e=request.POST.get('loginemail')
        login_s=request.POST.get('loginsenha')
        usuario= authenticate(username=login_e,password=login_s)
        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                return redirect('logado')
        else:
            request.method =='POST'
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            user=User.objects.filter(email=email)
            if nome ==None:
                return render(request,'index.html')
            if email ==None:
                return render(request,'index.html')
            if senha ==None:
                return render(request,'index.html')
            if user:
                return HttpResponse('Ja existe um usuario cadastro com este email')
            user=User.objects.create_user(username=nome,email=email,password=senha)
            user.save()
        return render (request,'index.html')

@login_required(login_url='home')
def logado(request):
    return render(request,'teste.html')
@login_required()
def logout_view(request):
    logout(request)
    return render(request,'index.html')
@login_required(login_url='home')
def agencia(request):
    txt_nome=request.GET.get('consulta')
    if txt_nome:
        consulta=IncomumAgencia.objects.filter(Q(age_codigo__icontains=txt_nome) | Q(age_cnpj__icontains=txt_nome) | Q(age_inscricaomunicipal__icontains=txt_nome))
    else:
        consulta=IncomumAgencia.objects.all()
    paginator = Paginator(consulta, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method=='GET':
        return render(request,'agencia.html',{'page_obj':page_obj})
    elif request.method == 'POST':
        codigo=request.POST.get('codigo')
        inscricao=request.POST.get('inscricao')
        cnpj=request.POST.get('cnpj')
        age_sites=request.POST.get('age_site')
        age_viagems=request.POST.get('age_viagem')
        situacao=request.POST.get('situacao')
        cep=request.POST.get('cep')
        rua=request.POST.get('rua')
        numero=request.POST.get('numero')
        bairro=request.POST.get('bairro')
        cidade=request.POST.get('cidade')
        fone=request.POST.get('fone')
        celular=request.POST.get('celular')
        comissao=request.POST.get('comissao')
        over=request.POST.get('over')
        markup=request.POST.get('markup')
        banco=request.POST.get('banco')
        agencias=request.POST.get('agencia')
        conta=request.POST.get('conta')
        tempo=time.strftime("%Y-%m-%d %H:%M")
        print(tempo)
        
        novo=IncomumAgencia.objects.create(age_site=age_sites,age_inscricaomunicipal=inscricao,age_cnpj=cnpj,age_viagem=age_viagems,age_datacadastro=tempo,age_situacao=situacao,age_cep=cep,age_rua=rua,age_numero=numero,age_bairro=bairro,age_cidade=cidade,age_fone=fone,age_celular=celular,age_comissao=comissao,age_over=over,age_markup=markup,age_banco=banco,age_agencia=agencias,age_conta=conta)
        print(novo)
        novo_id = novo.age_codigo

        return JsonResponse({'age_codigo': novo_id})
@login_required(login_url='home')
def agente(request):
    if request.method=='GET':
        return render(request,'agente.html')
    elif 1==1:
        age_codigo=request.POST.get('codigo')
        agt_descricao=request.POST.get('descricao')
        agt_cpf=request.POST.get('cpf')
        novo=IncomumAgente.objects.create(age_codigo=age_codigo,agt_descricao=agt_descricao,agt_cpf=agt_cpf)
        novo.save()
        return render(request,'agente.html')
    
def consulta(request):
    txt_nome = request.GET.get('consulta')
    if txt_nome:
        consulta = IncomumAgencia.objects.filter(Q(age_codigo__icontains=txt_nome) | 
                                                 Q(age_cnpj__icontains=txt_nome) | 
                                                 Q(age_inscricaomunicipal__icontains=txt_nome) | 
                                                 Q(age_descricao__icontains=txt_nome))
    else:
        consulta = IncomumAgencia.objects.all()
    
    # Paginação
    paginator = Paginator(consulta, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    
    # Prepara os dados para enviar como resposta JSON
    resultados = list(page.object_list.values())  # Converte os objetos do QuerySet para uma lista de dicionários
    return JsonResponse({'resultados': resultados})


        
        
from django.http import JsonResponse

def obter_novos_cadastros(request):
    novos_cadastros =IncomumAgencia.objects.all()
    novos_cadastros_serialized = [{'age_codigo': cadastro.age_codigo, 'age_descricao': cadastro.age_descricao, 'age_cnpj':cadastro.age_cnpj,'age_inscricaomunicipal':cadastro.age_inscricaomunicipal,'age_observacao':cadastro.age_observacao} for cadastro in novos_cadastros]
    return JsonResponse({'novos_cadastros': novos_cadastros_serialized})

from django.http import JsonResponse

def sua_view_de_consulta(request):
    consulta = request.GET.get('consulta')
    # Faça a consulta no banco de dados ou onde quer que seus dados estejam
    # Substitua este exemplo com sua lógica de consulta real
    resultados = [{'age_codigo': resultado.age_codigo, 'age_bairro': resultado.age_bairro,'age_cnpj':resultado.age_cnpj,'age_inscricaomunicipal':resultado.age_inscricaomunicipal,'age_viagem':resultado.age_viagem} for resultado in IncomumAgencia.objects.filter(Q(age_viagem__icontains=consulta))]
    print(resultados)
    return JsonResponse({'resultados': resultados})

def autocomplete_endereco(request):
    if request.method == 'GET':
        cep = request.GET.get('cep')
        
        # Faça a requisição à API de CEP
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/',verify=False)

        if response.status_code == 200:
            # A resposta foi bem-sucedida, trate os dados
            data = response.json()
            endereco = {
                'logradouro': data.get('logradouro', ''),
                'bairro': data.get('bairro', ''),
                'cidade': data.get('localidade', ''),
                'estado': data.get('uf', '')
            }

            # Retorne os dados em formato JSON
            return JsonResponse(endereco)
        else:
            # Se a requisição falhar, retorne uma mensagem de erro
            return JsonResponse({'error': 'CEP não encontrado'}, status=404)
            
@login_required(login_url='home')      
def excluir_cadastro(request, age_codigo):
    cadastro = IncomumAgencia.objects.get(age_codigo=age_codigo)
    # Lógica para excluir o cadastro...
    cadastro.delete()
    return render(request,'agencia.html')
    
@login_required(login_url='home')  
def relacao(request,age_codigo):
    # Lógica para buscar o cadastro pelo ID
    agencia =IncomumAgencia.objects.get(age_codigo=age_codigo)

    if request.method == 'POST':
        # Atualizar os campos com os dados do formulário
        agencia.age_banco = request.POST.get('banco')
        agencia.age_agencia = request.POST.get('agencia')
        agencia.age_conta = request.POST.get('conta')
        agencia.age_inscricaomunicipal = request.POST.get('inscricao')
        agencia.age_cnpj = request.POST.get('cnpj')
        agencia.age_site = request.POST.get('age_site')
        agencia.age_viagem = request.POST.get('age_viagem')
        agencia.age_situacao = request.POST.get('situacao')
        agencia.age_cep = request.POST.get('cep')
        agencia.age_rua = request.POST.get('rua')
        agencia.age_numero = request.POST.get('numero')
        agencia.age_bairro = request.POST.get('bairro')
        agencia.age_cidade = request.POST.get('cidade')
        agencia.age_fone = request.POST.get('fone')
        agencia.age_celular = request.POST.get('celular')
        agencia.age_comissao = request.POST.get('comissao')
        agencia.age_over = request.POST.get('over')
        agencia.age_markup = request.POST.get('markup')
        # Salvar as alterações no banco de dados
        agencia.save()
        # Redirecionar para uma nova página após a atualização
        return redirect('agencia')  # Altere para a página desejada

    # Se o método for GET, renderize a página de edição com os dados atuais do cadastro
    return render(request, 'agencias.html', {'agencia': agencia})
    
@login_required(login_url='home')
def faturamento(request):
    if request.method == 'GET':
        # Execute a consulta SQL personalizada
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT TO_CHAR(fim_data, 'MM/YYYY') AS mes_ano,
                    faturamentosimplificado.loj_codigo,
                    loj_descricao,
                    SUM(fim_valorliquido) AS soma_valorliquido,
                    SUM(fim_valorinc) AS soma_valorinc
                    FROM faturamentosimplificado
                    WHERE fim_codigo < 100
                    GROUP BY TO_CHAR(fim_data, 'MM/YYYY'), faturamentosimplificado.loj_codigo, loj_descricao;

            """)
            resultados = cursor.fetchall()
        
        # Formatar os resultados como necessário
            resultados_formatados = []
            for resultado in resultados:
                resultados_formatados.append({
                    'mes_ano':resultado[0],
                    'loj_descricao': resultado[2],
                    'soma_valorliquido': float(resultado[3]),  # Converte para float se necessário
                })

        # Retorne a renderização do template com os dados do faturamento no contexto
    return render(request, 'faturamentounidade.html', {'resultados': resultados_formatados})

@login_required(login_url='home')
def relatorio(request):
    return render(request,'relatorio.html')

def consulta_relatorio(request):
    if request.method == 'GET':
        data_consulta = request.GET.get('data_consulta')
        data_consulta_final = request.GET.get('data_final')
        unidade_selecionada = request.GET.get('unidade')

        # Verifica se o parâmetro de unidade foi fornecido
        if unidade_selecionada:
            # Se o parâmetro de unidade foi fornecido, inclua-o na consulta SQL
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM faturamentosimplificado WHERE loj_codigo = %s AND fim_data BETWEEN %s AND %s", [unidade_selecionada, data_consulta, data_consulta_final])
                resultados = cursor.fetchall()
        else:
            # Se o parâmetro de unidade não foi fornecido, execute a consulta sem ele
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM faturamentosimplificado WHERE fim_data BETWEEN %s AND %s", [data_consulta, data_consulta_final])
                resultados = cursor.fetchall()

        soma_valorliquido = sum(resultado[9] for resultado in resultados)
        soma_valorinc = sum(resultado[11] for resultado in resultados)
        soma_valorincajustado = sum(resultado[12] for resultado in resultados)

        resultados_formatados = [{
            'fim_tipo': resultado[7],
            'tur_numerovenda': resultado[8],
            'tur_codigo': resultado[1],
            'fim_valorliquido': resultado[9],
            'fim_markup': resultado[10],
            'fim_valorinc': resultado[11],
            'fim_valorincajustado': resultado[12],
            'aco_descricao': resultado[14]
        } for resultado in resultados]

        return JsonResponse({'resultados': resultados_formatados, 'soma_valorliquido': soma_valorliquido, 'soma_valorinc': soma_valorinc, 'soma_valorincajustado': soma_valorincajustado})


def exportar_excel(request):
    if request.method == 'GET':
        data_consulta = request.GET.get('data_consulta')
        data_consulta_final = request.GET.get('data_final')
        
        if data_consulta and data_consulta_final:
            # Execute a mesma consulta SQL personalizada
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM faturamentosimplificado WHERE fim_data BETWEEN %s AND %s", [data_consulta, data_consulta_final])
                resultados = cursor.fetchall()
            
            # Formatar os resultados como necessário
            resultados_formatados = [
                ["Tipo", "Num.Venda", "Num.Pct.", "Vlr Liq Venda", "MKP", "INC", "INC Ajustado", "Area Comercial"]
            ]
            for resultado in resultados:
                resultados_formatados.append([
                    resultado[7], resultado[8], resultado[1], resultado[9], resultado[10], resultado[11], resultado[12], resultado[14]
                ])
            
            # Criar o arquivo Excel
            wb = Workbook()
            ws = wb.active
            for row in resultados_formatados:
                ws.append(row)
            
            # Salvar o arquivo Excel
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=relatorio.xlsx'
            wb.save(response)
            
            return response
        else:
            return HttpResponse("Parâmetros de data ausentes")
