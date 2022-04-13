from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime, date

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    img = models.ImageField(null=True, blank=True, upload_to = "img")
    precio = models.IntegerField()
    specs = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    fecha_pub = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.titulo) +" | "+ str(self.autor)

    def get_absolute_url(self):
        return reverse("articulo", kwargs={"pk": self.pk})
    
    def get_img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url
        else:
            return None
