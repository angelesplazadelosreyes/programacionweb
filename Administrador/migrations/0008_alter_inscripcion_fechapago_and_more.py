# Generated by Django 4.0.5 on 2022-07-02 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0007_alter_galeria_url_alter_inscripcion_fechapago_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='fechaPago',
            field=models.DateField(default=datetime.datetime(2022, 7, 2, 13, 1, 8, 569741)),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='fechaActualizacion',
            field=models.DateField(default=datetime.datetime(2022, 7, 2, 13, 1, 8, 569741)),
        ),
        migrations.AlterField(
            model_name='salida',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2022, 7, 2, 13, 1, 8, 569741)),
        ),
        migrations.AlterField(
            model_name='salida',
            name='horaInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 2, 13, 1, 8, 569741)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecNacimiento',
            field=models.DateField(default=datetime.datetime(2022, 7, 2, 13, 1, 8, 553739)),
        ),
    ]
