from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Noticia (models.Model):
    id_noticia=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    imagen=models.CharField(max_length=100, default='')
    categoria=models.ForeignKey(categoria,on_delete=models.CASCADE)



class categoria (models.Model):
    id_categoria=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    