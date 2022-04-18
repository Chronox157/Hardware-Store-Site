from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import path, reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from datetime import datetime, date

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    img = models.ImageField(null=True, blank=True, upload_to = "img")
    precio = models.IntegerField()
    specs = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default="admin")
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

Tipo_pub = (
    ('Trabajo/Serv','Trabajo/Serv'),
    ('Pregunta', 'Pregunta'),
    ('General','General'),
)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=255)
    img = models.ImageField(null=True, blank=True, upload_to = "img")
    specs = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    fecha_pub = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=13, choices=Tipo_pub, default='General')

    def __str__(self):
        return str(self.tipo+" | "+self.titulo) +" | "+ str(self.autor)

    def get_absolute_url(self):
        return reverse("publicacion", kwargs={"pk": self.pk})
    
    def get_img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url
        else:
            return None

    class Meta:
        verbose_name_plural = "Publicaciones"

class Perfil(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = RichTextField(blank=True,null=True)
    img_perfil = models.ImageField(null=True, blank=True, upload_to="img/perfil")
    sitio_web = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Perfiles"

    def get_weburl(self):
        return str(self.sitio_web)

    def get_img_url(self):
        if self.img_perfil and hasattr(self.img_perfil, 'url'):
            return self.img_perfil.url
        else:
            return str("static\img\perfil.jpg")

    def __str__(self):
        return str(self.usuario)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(usuario=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.perfil.save()
