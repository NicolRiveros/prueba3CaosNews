from django.db import router
from rest_framework import routers, urlpatterns
from principal.viewsets import CategoriaViewset , NoticiaViewset , UsuarioViewset

router=routers.SimpleRouter()
router.register('Categoria', CategoriaViewset)
router.register('Noticia', NoticiaViewset)
router.register('Usuario', UsuarioViewset)

urlpatterns=router.urls