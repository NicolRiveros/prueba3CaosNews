from django.db import router
from rest_framework import routers, urlpatterns
from principal.viewsets import CategoriaViewset

router=routers.SimpleRouter()
router.register('Categoria', CategoriaViewset)

urlpatterns=router.urls