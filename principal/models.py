from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Noticia (models.Model):
    id_noticia=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    imagen=models.CharField(max_length=100, default='')