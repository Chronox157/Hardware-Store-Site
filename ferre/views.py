
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ferre.models import Articulo, Publicacion
from .forms import ArticuloForm, PublicacionForm

###Articulos

def HomeView(request):
        articulos = Articulo.objects.all()[0:3]
        restantes = Articulo.objects.all().count() - 3
        
        if restantes < 0:
            restantes = 0
        dicc = {
            "art" : articulos,
            "rest" : restantes
        }
        
        return render(request, "home.html", dicc)

class MenuArticulos(ListView):
    model = Articulo
    template_name = "articulos/lista_articulos.html"
    ordering = ['-fecha_pub']

def BuscarArticuloView(request):
    #busqueda = None
    if request.method == "POST":
        busqueda = request.POST.get('busqueda', False)
        resultados = Articulo.objects.filter(titulo__icontains=busqueda)
        context = {'busqueda' : busqueda, 'resultados' : resultados}

        return render(request, "articulos/buscar_articulo.html", context)

    else:
        return render(request, "articulos/buscar_articulo.html", {})
 
class ArticuloView(DetailView):
    model = Articulo
    template_name = "articulos/articulo_detalle.html"
    context_object_name = 'post'

class CrearArticuloView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = "articulos/crear_articulo.html"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarArticuloView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulos/editar_articulo.html'
    context_object_name = 'post'

class EliminarArticuloView(DeleteView):
    model = Articulo
    template_name = 'articulos/eliminar_articulo.html'
    success_url = reverse_lazy('home')
    context_object_name = 'post'

###Publicaciones

class MenuPubli(ListView):
    model = Publicacion
    template_name = "publicaciones/lista_publi.html"
    ordering = ['-fecha_pub']

    def get_context_data(self, **kwargs):

        dicc = super().get_context_data(**kwargs)
        dicc["Trabajo_Serv"] = Publicacion.objects.filter(tipo__contains="Trabajo/Serv")
        dicc["Pregunta"] = Publicacion.objects.filter(tipo__contains="Pregunta")
        dicc["General"] = Publicacion.objects.filter(tipo__contains="General")

        return dicc 

class PublicacionView(DetailView):
    model = Publicacion
    template_name = "publicaciones/publi_detalle.html"
    context_object_name = 'post'

class EditarPubliView(UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = 'publicaciones\editar_publi.html'
    context_object_name = 'post'

class CrearPubliView(CreateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = "articulos/crear_articulo.html"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EliminarPubliView(DeleteView):
    model = Publicacion
    template_name = 'publicaciones\eliminar_publi.html'
    success_url = reverse_lazy('lista_publi')
    context_object_name = 'post'


def MiPerfil(request):
    return render(request, "miperfil.html", {})
    