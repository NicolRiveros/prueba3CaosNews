from django import http
from principal.models import Noticia
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Noticia
from .models import Categoria
from django.core.files.storage import FileSystemStorage #PERMITE ACCEDER AL SISTEMA DE ARCHIVOS

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
    try:
        v_titulo=request.POST.get('titulo')
        v_idNoticia=request.POST.get('idNoticia')
        v_encabezado=request.POST.get('encabezado')
        v_descripcion=request.POST.get('descripcion')
        v_categoria=request.POST.get('categoria')

        #RESCATA EL OBJETO IMAGEN DEL FORMULARIO
        v_imagen=request.FILES.get('imagen')
        fs = FileSystemStorage()
        file = fs.save(v_imagen.name, v_imagen)
        #FILE ES EL NOMBRE DEL ARCHIVO

        categoria=Categoria.objects.get(idCategoria=v_categoria)

        nuevo=Noticia()
        nuevo.titulo=v_titulo
        nuevo.idNoticia=v_idNoticia
        nuevo.encabezado=v_encabezado
        nuevo.descripcion=v_descripcion
        nuevo.categoria=categoria
        nuevo.imagen=file

        Noticia.save(nuevo)
        return redirect('/noticias')
    except Exception as e:
        return HttpResponse(e)

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
    return redirect('/noticias')

def eliminarNoticia(request, v_idNoticia):
    noticia=Noticia.objects.get(idNoticia=v_idNoticia)

    Noticia.delete(noticia)
    return redirect('/noticias')
    #return HttpResponse('Id del producto: ' + str(v_idNoticia))

def modificarNoticia(request, v_idNoticia):
    noticia=Noticia.objects.get(idNoticia=v_idNoticia)
    categoria=Categoria.objects.all()
    context={'datos': noticia, 'categorias': categoria}
    return render(request, 'formModificar.html', context)

def guardarModificarNoticia(request):
    try:
        v_titulo=request.POST.get('titulo')
        v_idNoticia=request.POST.get('idNoticia')
        v_encabezado=request.POST.get('encabezado')
        v_descripcion=request.POST.get('descripcion')
        v_categoria=request.POST.get('categoria')

        v_imagen=request.FILES.get('imagen')
        fs = FileSystemStorage()
        file = fs.save(v_imagen.name, v_imagen)

        categoria=Categoria.objects.get(idCategoria=v_categoria)
        noticia=Noticia.objects.get(idNoticia=v_idNoticia)

        noticia.titulo=v_titulo
        noticia.encabexado=v_encabezado
        noticia.descripcion=v_descripcion
        noticia.categoria=categoria
        noticia.imagen=file

        Noticia.save(noticia)
        return redirect('/noticias')
    except Exception as e:
        return HttpResponse(e)
