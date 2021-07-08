from django.db.models import fields
from principal.models import Categoria, Noticia, Usuario 
from rest_framework import serializers


class CategoriaSerializer (serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields = '__all__'
   
class NoticiaSerializer (serializers.ModelSerializer):
    class Meta:
        model=Noticia
        fields = '__all__'

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields = '__all__'