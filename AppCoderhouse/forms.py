from django import forms
from .models import Profile


class articuloformulario(forms.Form):
    tipo_articulo = forms.CharField()
    stock = forms.IntegerField()
    criterio_nombre = forms.CharField(max_length=100)

class ProfileForm(forms.ModelForm):
    imagen = forms.ImageField(widget=forms.FileInput, required=False)
    
    class Meta:
        model = Profile
        fields = ['imagen', 'info']