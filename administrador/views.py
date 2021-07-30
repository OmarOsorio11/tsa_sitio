from django.core.exceptions import PermissionDenied
from administrador.models import Producto
from django.shortcuts import redirect, render
from django.views import generic
from .models import Categoria, Cotizacion
from .forms import CotizacionForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def solicitudok(request):
    return render(request,'solicitudok.html')

def cotizar(request, Producto):
    if request.method == "POST": 
        nombreCliente=request.POST['nombre_cliente']
        direccionCliente=request.POST['direccion_cliente']
        telefonoCliente=request.POST['telefono_cliente']
        cantidadProducto=int(request.POST['cantidad_producto'])

        obj = Cotizacion(nombre_cliente=nombreCliente, direccion_cliente=direccionCliente, telefono_cliente=telefonoCliente, producto=Producto, cantidad=cantidadProducto)
        obj.save()
        return redirect('solicitudok')
            
                
    else:
        form = CotizacionForm()
    return render(request,'cotizacion.html',{'form':form,'prod':Producto})




def producto(request, producto):
    prod=Producto.objects.filter(nombre__exact=producto)
    for p in prod:
        if p.moneda=="DOLAR":
            p.dolar=True
        else:
            p.dolar=False

        total_formt=str(p.precio)
        if len(total_formt)>6:
            p.precio=total_formt[0:len(total_formt)-6]+","+total_formt[len(total_formt)-6:len(total_formt)-3]+","+total_formt[len(total_formt)-3:]
        elif len(total_formt)>3:
            p.precio=total_formt[0:len(total_formt)-3]+","+total_formt[len(total_formt)-3:]
        else: 
            p.precio=total_formt
        txt=p.nombre
        specialChars = "-/ ." 
        for specialChar in specialChars:
            txt = txt.replace(specialChar, '')

        p.url_img="img/imagenes/"+txt+".png"
    return render(request,'producto.html',{'prod':prod})

def productos(request, categoria):
    #prod=Producto.objects.filter(supercategoria__exact=categoria)
    categorias=Categoria.objects.filter(nombre__exact=categoria)
    id_cate=categorias[0].id
    prod=Producto.objects.filter(supercategoria__exact=id_cate)
    for p in prod:
        if p.moneda=="DOLAR":
            p.dolar=True
        else:
            p.dolar=False

        total_formt=str(p.precio)
        if len(total_formt)>6:
            p.precio=total_formt[0:len(total_formt)-6]+","+total_formt[len(total_formt)-6:len(total_formt)-3]+","+total_formt[len(total_formt)-3:]
        elif len(total_formt)>3:
            p.precio=total_formt[0:len(total_formt)-3]+","+total_formt[len(total_formt)-3:]
        else: 
            p.precio=total_formt
        txt=p.nombre
        specialChars = "-/ ." 
        for specialChar in specialChars:
            txt = txt.replace(specialChar, '')

        p.url_img="img/imagenes/"+txt+".png"

    cat=Categoria.objects.filter(nombre__exact=categoria)
    
    for c in cat:
        c.url="img/CATEGORIAS/"+c.nombre+".png"
    return render(request,'productos.html', {'cat':cat,'prod':prod})


def catalogo(request):
    cat=Categoria.objects.filter()
    for c in cat:
        c.url="img/CATEGORIAS/"+c.nombre+".png"
    
    return render(request,'categorias.html',{'categorias':cat})
