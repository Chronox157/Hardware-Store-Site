from django.urls import path
from .views import CrearPubliView, EditarArticuloView, HomeView, ArticuloView, CrearArticuloView, EliminarArticuloView, BuscarArticuloView, MenuArticulos, MenuPubli, PublicacionView, EditarPubliView
from . import views

urlpatterns = [
    path('', HomeView, name="home"),
    path('articulo', MenuArticulos.as_view(), name="lista_articulos"),
    path("articulo/<int:pk>/", ArticuloView.as_view(), name="articulo"),
    path("articulo/crear/", CrearArticuloView.as_view(), name="crearArt"),
    path("articulo/editar/<int:pk>/", EditarArticuloView.as_view(), name="editarArt"),
    path("articulo/eliminar/<int:pk>/", EliminarArticuloView.as_view(), name="eliminarArt"),
    path("articulo/buscar", BuscarArticuloView, name="buscarArt"),

    path("publicacion/", MenuPubli.as_view(), name="lista_publi"),
    path("publicacion/<int:pk>/", PublicacionView.as_view(), name="publicacion"),
    path("publiacion/editar/<int:pk>", EditarPubliView.as_view(), name="editarPubli"),
    path("publicacion/crear/", CrearPubliView.as_view(), name="crearPubli"),
    path("miperfil/", views.MiPerfil, name="miperfil"),

]
