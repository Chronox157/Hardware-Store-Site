from django.contrib.auth.models import User
from ferre.models import Perfil

users = User.objects.filter(perfil=None)
for user in users:
    Perfil.objects.create(usuario=user)