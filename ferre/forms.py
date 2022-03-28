from tkinter import Widget
from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ('titulo', 'img', 'specs', 'autor', 'body')

        widget = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'specs' : forms.TextInput(attrs={'class': 'form-control'}),
            'autor' : forms.Select(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),

    }