from principal.models import Categoria 
from rest_framework import viewsets
from principal.serializer import CategoriaSerializer 


class CategoriaViewset (viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class=CategoriaSerializer
     