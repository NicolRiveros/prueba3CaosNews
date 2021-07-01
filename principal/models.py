from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True)
    nombreCategoria=models.CharField(max_length=100, verbose_name='Nombre categoria')

class Noticia(models.Model):
    idNoticia=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')
    encabezado=models.CharField(max_length=100, verbose_name='Encabezado')
    descripcion=models.CharField(max_length=900, verbose_name='Contenido')

    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    