# Generated by Django 3.2.4 on 2021-07-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0011_auto_20210707_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='direccion_cliente',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='producto',
            field=models.TextField(),
        ),
    ]