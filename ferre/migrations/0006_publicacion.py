# Generated by Django 4.0.3 on 2022-04-16 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferre', '0005_alter_articulo_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('articulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ferre.articulo')),
            ],
            bases=('ferre.articulo',),
        ),
    ]
