from django.urls import path
from .views import EditarArticuloView, HomeView, ArticuloView, CrearArticuloView, EliminarArticuloView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("articulo/<int:pk>/", ArticuloView.as_view(), name="articulo"),
    path("miperfil/", views.MiPerfil, name="miperfil"),
    path("articulo/crear/", CrearArticuloView.as_view(), name="crearArt"),
    path("articulo/editar/<int:pk>/", EditarArticuloView.as_view(), name="editarArt"),
    path("articulo/eliminar/<int:pk>/", EliminarArticuloView.as_view(), name="eliminarArt")

]
