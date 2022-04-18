from django.urls import path
from .views import CrearUsuarioView, EditarUsuarioView, VerUsuarioView, EditarPerfilView
from django.contrib.auth import views as auth_view

urlpatterns = [
path("register/", CrearUsuarioView.as_view(), name="registro"),
path("perfil/<int:id>", VerUsuarioView, name="usuario"),
path("editar_usuario/", EditarUsuarioView.as_view(), name="editarUser"),
path("editar_usuario/perfil", EditarPerfilView.as_view(), name="editarPerf"),
path("password/", auth_view.PasswordChangeView.as_view()),

]
