from django.urls import path
from .views import EditarArticuloView, HomeView, ArticuloView, CrearArticuloView, EliminarArticuloView, BuscarArticuloView, MenuArticulos, MenuPubli
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
    path("miperfil/", views.MiPerfil, name="miperfil"),

]
