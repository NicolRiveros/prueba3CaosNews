from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True)
    nombreCategoria=models.CharField(max_length=100, verbose_name='Nombre categoria')

class Noticia(models.Model):
    idNoticia=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')
    descripcion=models.CharField(max_length=300, verbose_name='Informacion')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    