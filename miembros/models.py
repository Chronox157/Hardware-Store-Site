from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.forms import TimeField

from ferre.models import Articulo


class ComentarioArticulo(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="comentarios")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pub = models.TimeField(auto_now_add=True)
    body = RichTextField()

    class Meta:
        ordering = ["fecha_pub"]

    def __str__(self):
        return str(self.usuario.first_name +" | Comentario")