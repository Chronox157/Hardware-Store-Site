from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrarseForm(UserCreationForm):
    email = forms.EmailField()
    nombre= forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)

    class Meta:
        model = User
        #fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        fields = UserCreationForm.Meta.fields + ('nombre', 'apellido', 'email')


