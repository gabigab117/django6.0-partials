from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})

def single_post_partial(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # C'est ici que la magie opère : on cible le partial avec #card
    return render(request, "blog/index.html#card", {"post": post})

def home(request):
    post = Post.objects.first()
    return render(request, "blog/home.html", {"post": post})

