# Generated by Django 4.2.1 on 2023-06-24 00:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_detalle_imagen_detalle_nombre_alter_detalle_cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='estado',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='detalle',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 6, 23, 20, 53, 24, 320367)),
        ),
        migrations.AddField(
            model_name='detalle',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
