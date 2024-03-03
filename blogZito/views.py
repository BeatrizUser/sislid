from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    # Recupere todas as postagens ordenadas pela data de publicação
    posts = Post.objects.order_by('-published_date')
    # Renderize o template 'blog_home.html' e passe as postagens para ele
    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})