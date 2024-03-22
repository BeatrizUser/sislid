from .models import Pergunta
from .forms import PerguntaForm
from django.shortcuts import render, redirect


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

def formulario(request):
    if request.method == 'POST':
        form = PerguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario')
    else:
        form = PerguntaForm()
    perguntas = Pergunta.objects.all()
    return render(request, 'formulario.html', {'form': form, 'formulario': formulario})