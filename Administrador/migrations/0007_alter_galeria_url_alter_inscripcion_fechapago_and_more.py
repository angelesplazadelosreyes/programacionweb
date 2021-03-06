# Generated by Django 4.0.5 on 2022-07-02 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0006_alter_inscripcion_fechapago_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='url',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='fechaPago',
            field=models.DateField(default=datetime.datetime(2022, 7, 2, 12, 57, 28, 392010)),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='fechaActualizacion',
            field=models.DateField(default=datetime.datetime(2022, 7, 2, 12, 57, 28, 392010)),
        ),
        migrations.AlterField(
            model_name='salida',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2022, 7, 2, 12, 57, 28, 392010)),
        ),
        migrations.AlterField(
            model_name='salida',
            name='horaInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 2, 12, 57, 28, 392010)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecNacimiento',
            field=models.DateField(default=datetime.datetime(2022, 7, 2, 12, 57, 28, 392010)),
        ),
    ]
