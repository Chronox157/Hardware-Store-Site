# Generated by Django 4.0.3 on 2022-04-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferre', '0006_alter_perfil_img_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='sitio_web',
            field=models.URLField(blank=True, null=True),
        ),
    ]