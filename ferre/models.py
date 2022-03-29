from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    img = models.ImageField(null=True, blank=True, upload_to = "img")
    precio = models.IntegerField()
    specs = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    fecha_pub = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.titulo) +" | "+ str(self.autor)

    def get_absolute_url(self):
        return reverse("articulo", kwargs={"pk": self.pk})
    
