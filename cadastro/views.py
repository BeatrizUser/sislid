from django.http import JsonResponse
import requests
from django.shortcuts import render, redirect
from .models import Pergunta
from .forms import PerguntaForm

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
    return JsonResponse({'error': 'CEP não encontrado'}, status=400)

def perguntas(request):
    if request.method == 'POST':
        form = PerguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perguntas')
    else:
        form = PerguntaForm()
    perguntas = Pergunta.objects.all()
    return render(request, 'perguntas.html', {'form': form, 'perguntas': perguntas})

