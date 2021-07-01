from django import http
from principal.models import Noticia
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Noticia
from .models import Categoria
# Create your views here.

def principal(request):
    return render(request, 'Principal.html')

def verNoticias(request):
    noticias=Noticia.objects.all()
    datos={'noticias': noticias}

    return render(request, 'verNoticias.html', datos)

def formNoticia(request):
    categoria=Categoria.objects.all()
    contexto={'categorias': categoria}
    return render(request, 'formNoticias.html', contexto)


def guardarNoticia(request):
    v_titulo=request.POST.get('titulo')
    v_idNoticia=request.POST.get('idNoticia')
    v_encabezado=request.POST.get('encabezado')
    v_descripcion=request.POST.get('descripcion')
    v_categoria=request.POST.get('categoria')

    categoria=Categoria.objects.get(idCategoria=v_categoria)

    nuevo=Noticia()
    nuevo.titulo=v_titulo
    nuevo.idNoticia=v_idNoticia
    nuevo.encabezado=v_encabezado
    nuevo.descripcion=v_descripcion
    nuevo.categoria=categoria

    Noticia.save(nuevo)
    return redirect('/noticias')

def formCategoria(request):
    return render(request, 'formCategoria.html')

def guardarCategoria(request):
    v_idCategoria=request.POST.get('idCategoria')
    v_nombreCategoria=request.POST.get('nombreCategoria')

    nuevoCate=Categoria()
    nuevoCate.idCategoria=v_idCategoria
    nuevoCate.nombreCategoria=v_nombreCategoria

    Categoria.save(nuevoCate)

    categoria=Categoria.objects.all()

    context={'categoria': categoria}
    return HttpResponse('Categoria Agregada:' + v_nombreCategoria)