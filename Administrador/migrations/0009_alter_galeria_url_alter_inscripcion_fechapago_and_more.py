# Generated by Django 4.0.5 on 2022-07-03 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0008_alter_inscripcion_fechapago_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='fechaPago',
            field=models.DateField(default=datetime.datetime(2022, 7, 3, 0, 59, 33, 908949)),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='descripcion',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='fechaActualizacion',
            field=models.DateField(default=datetime.datetime(2022, 7, 3, 0, 59, 33, 908949)),
        ),
        migrations.AlterField(
            model_name='salida',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2022, 7, 3, 0, 59, 33, 908949)),
        ),
        migrations.AlterField(
            model_name='salida',
            name='horaInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 0, 59, 33, 908949)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecNacimiento',
            field=models.DateField(default=datetime.datetime(2022, 7, 3, 0, 59, 33, 908949)),
        ),
    ]
