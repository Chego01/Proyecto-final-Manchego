from django import forms
 
class articuloformulario(forms.Form):
    tipo_articulo = forms.CharField()
    stock = forms.IntegerField()

class clienteformulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class empleadoformulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.CharField()
   