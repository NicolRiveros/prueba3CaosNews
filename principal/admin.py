from django.contrib import admin
from principal.models import Categoria
from principal.models import Noticia

#REGISTRAR LOS MODELO
#PARA QUE SE PUEDAN DESPLEGAR Y MOSTRAR
class NoticiaAdmin(admin.ModelAdmin):
    list_display=("titulo", "encabezado" ,"descripcion")

class CategoriaNoAdmin(admin.ModelAdmin):
    list_display=("nombreCategoria", "idCategoria")


#REGISTRAR LOS MODELO
admin.site.register(Categoria, CategoriaNoAdmin) 
admin.site.register(Noticia, NoticiaAdmin)



