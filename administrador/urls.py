from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('productos/<categoria>/', views.productos, name='productos'),
    path('producto/<producto>/', views.producto, name='producto'),
    path('cotizar/<Producto>/', views.cotizar, name='cotizar'),
    path('solicitudok/',views.solicitudok,name='solicitudok')
]