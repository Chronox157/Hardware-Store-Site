# Generated by Django 4.0.3 on 2022-04-18 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]
