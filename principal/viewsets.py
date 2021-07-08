from principal.models import Categoria, Noticia, Usuario 
from rest_framework import viewsets
from principal.serializer import CategoriaSerializer, NoticiaSerializer, UsuarioSerializer 


class CategoriaViewset (viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class=CategoriaSerializer

class NoticiaViewset (viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class=NoticiaSerializer

class UsuarioViewset (viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class=UsuarioSerializer
     