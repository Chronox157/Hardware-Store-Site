# Generated by Django 4.0.3 on 2022-04-04 18:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ferre', '0004_articulo_fecha_pub_alter_articulo_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]