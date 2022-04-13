from django.urls import path
from .views import CrearUsuarioView

urlpatterns = [
path("register/", CrearUsuarioView.as_view(), name="registro")

]
