from django.urls import path
from .views import CrearUsuarioView, EditarPerfilView, VerUsuarioView
from django.contrib.auth import views as auth_view

urlpatterns = [
path("register/", CrearUsuarioView.as_view(), name="registro"),
path("perfil/<int:id>", VerUsuarioView, name="usuario"),
path("editar_perfil/", EditarPerfilView.as_view(), name="editarPerf"),
path("password/", auth_view.PasswordChangeView.as_view()),

]
