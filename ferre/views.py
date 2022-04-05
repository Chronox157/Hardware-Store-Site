from multiprocessing import context
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ferre.models import Articulo
from .forms import ArticuloForm
import calendar


class HomeView(ListView):
    model = Articulo
    template_name = "home.html"
    ordering = ['-fecha_pub']

class ArticuloView(DetailView):
    model = Articulo
    template_name = "articulos/articulo_detalle.html"
    context_object_name = 'post'

class CrearArticuloView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = "articulos/crear_articulo.html"
    #fields = '__all__'

class EditarArticuloView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulos/editar_articulo.html'
    #ields = ['titulo', 'precio', 'specs', 'body']
    context_object_name = 'post'

class EliminarArticuloView(DeleteView):
    model = Articulo
    template_name = 'articulos/eliminar_articulo.html'
    success_url = reverse_lazy('home')


def MiPerfil(request):
    return render(request, "miperfil.html", {})
    