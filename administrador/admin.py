from django.contrib import admin
from .models import Categoria, Moneda, Producto, Cotizacion
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'descripcion')
    

#admin.site.register(Categoria,CategoriaAdmin)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('supercategoria','nombre','precio','moneda','caracteristicas')
    list_filter =('nombre','supercategoria','moneda')

@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display=('nombre_cliente','direccion_cliente','telefono_cliente','producto','cantidad')

@admin.register(Moneda)
class MonedaAdmin(admin.ModelAdmin):
    list_display=('nombre',)

