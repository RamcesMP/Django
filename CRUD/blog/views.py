from django.shortcuts import render
from .models import Post,Categoria

# Create your views here.

def blog(request):
    categorias=Categoria.objects.all()
    posts=Post.objects.all()
    data={
        "posts":posts,
        "categorias":categorias,
    }
    return render(request,"blog/blog.html",data)

def categoria(request,categoria_id):
    categorias=Categoria.objects.all()
    categoria=categoria_id
    posts=Post.objects.filter(categorias=categoria)
    data={
        "posts":posts,
        "categorias":categorias,
    }
    return render(request,"blog/blog.html",data)