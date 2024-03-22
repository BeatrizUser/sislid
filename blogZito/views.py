from django.shortcuts import render, get_object_or_404
from .models import Post
from gabineteOnline.forms import PerguntaForm
from django import forms

def home(request):
    # Recupere todas as postagens ordenadas pela data de publicação
    posts = Post.objects.order_by('-published_date')
    # Verifique se o método de requisição é POST
    if request.method == 'POST':
        form = PerguntaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PerguntaForm()
    # Renderize o template 'index.html' e passe o formulário e as postagens para ele
    return render(request, 'home.html', {'form': form, 'posts': posts})

def sobre(request):
     # Recupere todas as postagens ordenadas pela data de publicação
    posts = Post.objects.order_by('-published_date')
    # Verifique se o método de requisição é POST
    if request.method == 'POST':
        form = PerguntaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PerguntaForm()
    return render(request, 'sobre.html', {'form': form, 'posts': posts})

def propostas(request):
     # Recupere todas as postagens ordenadas pela data de publicação
    posts = Post.objects.order_by('-published_date')
    # Verifique se o método de requisição é POST
    if request.method == 'POST':
        form = PerguntaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PerguntaForm()

    return render(request, 'propostas.html', {'form': form, 'posts': posts})

def blog(request):
    # Verifique se o método de requisição é POST
    if request.method == 'POST':
        form = PerguntaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PerguntaForm()

    posts = Post.objects.order_by('-published_date')
    
    return render(request, 'blog.html', {'form': form, 'posts': posts})

def post_detail(request, post_id):
     # Verifique se o método de requisição é POST
    if request.method == 'POST':
        form = PerguntaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PerguntaForm()

    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'form': form,'post': post})