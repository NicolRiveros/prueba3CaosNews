from django.db.models import fields
from django.db.models.base import Model
from principal.models import Noticia , Categoria , Usuario
from rest_framework import serializers


class CategoriaSerializer (serializers.ModelSerializer):
    class Meta:
        Model=Categoria
        fields='__all__'


class NoticiaSerializer (serializers.ModelSerializer):
    class Meta:
        Model=Noticia
        fields='__all__'


class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        Model=Usuario
        fields='__all__'        