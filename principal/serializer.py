from django.db.models import fields
from principal.models import Categoria 
from rest_framework import serializers


class CategoriaSerializer (serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields = '__all__'
   