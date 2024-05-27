from django.http import JsonResponse
import requests
from django.shortcuts import render, redirect
from .models import Pessoa, Lideranca

def sucesso(request):
    return render(request, 'formulario_sucess.html')

def formulario(request):
    # Carrega as lideranças disponíveis
    liderancas = Lideranca.objects.all()
    return render(request, 'formulario.html', {'liderancas': liderancas})

def cadastrar_pessoa(request):
    if request.method == 'POST':
        # Obter os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        cep = request.POST.get('cep')
        lideranca_id = request.POST.get('lideranca')

        # Verificar se todos os campos obrigatórios foram preenchidos (adicione mais validações conforme necessário)
        if nome and cidade and estado and cep and lideranca_id:
            # Verificar se o título eleitoral já existe no banco de dados
            titulo_eleitor = request.POST.get('titulo_eleitor')
            if Pessoa.objects.filter(titulo_eleitor=titulo_eleitor).exists():
                return render(request, 'formulario.html', {'error_message': 'Já existe uma pessoa cadastrada com este título eleitoral.', 'highlight_field': 'titulo_eleitor'})

            # Criar e salvar a pessoa no banco de dados
            lideranca = Lideranca.objects.get(id=lideranca_id)
            pessoa = Pessoa(nome=nome, email=email, cidade=cidade, estado=estado, cep=cep, lideranca=lideranca)
            pessoa.save()

            # Redirecionar para uma URL de sucesso
            return redirect('formulario_sucess.html')
        else:
            # Se algum campo obrigatório não foi preenchido, exibir uma mensagem de erro ou redirecionar de volta para o formulário com uma mensagem de erro
            # Carrega as lideranças disponíveis novamente para exibição no formulário
            liderancas = Lideranca.objects.all()
            return render(request, 'formulario.html', {'liderancas': liderancas, 'error_message': 'Por favor, preencha todos os campos obrigatórios.'})
    else:
        # Se o método HTTP não for POST, apenas renderize o formulário
        # Carrega as lideranças disponíveis para exibição no formulário
        liderancas = Lideranca.objects.all()
        return render(request, 'formulario.html', {'liderancas': liderancas})


def consultar_endereco(request):
    if request.method == 'GET' and request.is_ajax():
        cep = request.GET.get('cep')
        if cep:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            if response.status_code == 200:
                data = response.json()
                endereco = {
                    'rua': data.get('logradouro', ''),
                    'bairro': data.get('bairro', ''),
                    'cidade': data.get('localidade', ''),
                    'estado': data.get('uf', '')
                }
                return JsonResponse(endereco)
            else:
                return JsonResponse({'error': 'CEP não encontrado'}, status=400)
    return JsonResponse({'error': 'Requisição inválida'}, status=400)
