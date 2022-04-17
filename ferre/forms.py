from django import forms
from .models import Articulo, Publicacion

class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ('titulo','precio', 'img', 'specs', 'body')

        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.NumberInput(attrs={'class':'form-control'}),
            'specs' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),

    }

class PublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ('titulo', 'img', 'specs', 'body', 'tipo' )

        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.NumberInput(attrs={'class':'form-control'}),
            'specs' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),

    }

        


