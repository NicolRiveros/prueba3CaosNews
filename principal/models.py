from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True)
    nombreCategoria=models.CharField(max_length=100)

class Noticia(models.Model):
    idNoticia=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    