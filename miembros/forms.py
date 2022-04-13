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

        # widgets = {
        #     'username' : forms.TextInput(attrs={
        #         'class' : 'form-control'
        #     }),
        #     'nombre' : forms.TextInput(attrs={
        #         'class' : 'form-control'
        #     }),
        #     'apellido' : forms.TextInput(attrs={
        #         'class' : 'form-control'
        #     }),
        #     'password01' : forms.PasswordInput(attrs={
        #         'class' : 'form-control'
        #     }),
        #     'password02' : forms.PasswordInput(attrs={
        #         'class' : 'form-control'
        #     })
        # }

