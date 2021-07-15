from django import forms
from django.forms import Textarea, TextInput
from django.forms.widgets import NumberInput
from .models import Cotizacion

class CotizacionForm(forms.ModelForm):
    class Meta:
        model= Cotizacion
        fields=('nombre_cliente', 'direccion_cliente', 'telefono_cliente','cantidad')
        labels = {
            "nombre_cliente": ("Nombre del Cliente"),
            "dir_cliente": ("Dirección"),
            "telefono":("Teléfono")
        }
        
        widgets = {
            'nombre_cliente': TextInput(attrs={'class':'input'}),
            'direccion_cliente': Textarea(attrs={'class':'inputArea'}),
            'telefono_cliente': NumberInput(attrs={'class':'inputNum'}),
            'cantidad':NumberInput(attrs={'class':'inputNum'}),
        }