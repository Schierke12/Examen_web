# Generated by Django 4.2.1 on 2023-06-24 01:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_detalle_estado_detalle_fecha_detalle_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='estado',
            field=models.CharField(choices=[('en preparacion', 'EN PREPARACION'), ('saliendo de la sucursal', 'SALIENDO DE LA SUCURSAL'), ('en camino', 'EN CAMINO'), ('entregado', 'ENTREGADO')], default='en preparacion', max_length=30),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 6, 23, 21, 25, 28, 834073)),
        ),
    ]
