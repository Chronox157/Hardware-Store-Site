from re import template
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistrarseForm

class CrearUsuarioView(generic.CreateView):
    form_class = RegistrarseForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
