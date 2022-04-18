from re import template
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render
from django.contrib.auth.models import User
from ferre.models import Articulo, Perfil
from .forms import RegistrarseForm, EditarUsuarioForm, EditarPerfilForm

class CrearUsuarioView(generic.CreateView):
    form_class = RegistrarseForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class EditarUsuarioView(generic.UpdateView):
    form_class = EditarUsuarioForm
    template_name = "perfil/editar_usuario.html"
    success_url = reverse_lazy('lista_publi')

    def get_object(self):
        return self.request.user

class EditarPerfilView(generic.UpdateView):
    model = Perfil
    form_class = EditarPerfilForm
    template_name = "perfil/editar_perfil.html"
    success_url = reverse_lazy('editarUser')

    def get_object(self):
        return self.request.user.perfil


# class VerUsuarioView(generic.ListView):
#     model = Perfil
#     template_name = "perfil/ver_perfil.html"
#     context_name = "post"

def VerUsuarioView(request, id):
    usuario = User.objects.get(id = id)
    productos = Articulo.objects.filter(autor__id = id)
    context = {
    'usuario_vista': usuario,
    'productos': productos,
    }  
    return render(request, 'perfil/ver_perfil.html', context)