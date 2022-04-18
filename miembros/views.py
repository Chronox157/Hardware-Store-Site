from re import template
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render

from ferre.models import Perfil
from .forms import RegistrarseForm, EditarPerfilForm

class CrearUsuarioView(generic.CreateView):
    form_class = RegistrarseForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class EditarPerfilView(generic.UpdateView):
    form_class = EditarPerfilForm
    template_name = "perfil/editar_perfil.html"
    success_url = reverse_lazy('lista_publi')

    def get_object(self):
        return self.request.user

# class VerUsuarioView(generic.ListView):
#     model = Perfil
#     template_name = "perfil/ver_perfil.html"
#     context_name = "post"

def VerUsuarioView(request, id):
    user = Perfil.objects.get(id = id)
    context = {
    'user': user
    }  
    return render(request, 'perfil/ver_perfil.html', context)