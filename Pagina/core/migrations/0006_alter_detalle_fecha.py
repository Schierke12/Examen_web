# Generated by Django 4.2.1 on 2023-07-04 02:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_detalle_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 7, 3, 22, 42, 53, 983166)),
        ),
    ]
