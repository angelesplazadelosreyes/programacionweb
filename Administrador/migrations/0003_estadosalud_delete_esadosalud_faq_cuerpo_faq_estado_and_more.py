# Generated by Django 4.0.5 on 2022-07-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0002_acceso_esadosalud_faq_galeria_inscripcion_mensaje_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoSalud',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('peso', models.IntegerField()),
                ('estatura', models.IntegerField()),
                ('probCardiaco', models.CharField(default='', max_length=100)),
                ('probPresion', models.CharField(default='', max_length=100)),
                ('movilidad', models.CharField(default='', max_length=100)),
                ('otrosPob', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='EsadoSalud',
        ),
        migrations.AddField(
            model_name='faq',
            name='cuerpo',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='faq',
            name='estado',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='faq',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='galeria',
            name='estado',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='galeria',
            name='prioridad',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='galeria',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='galeria',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='codigoTb',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='estado',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='estadoPago',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='tipoPago',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='correo',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='cuerpo',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='estado',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='tipo',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='menu',
            name='nombre',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='noticia',
            name='bajada',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='noticia',
            name='cuerpo',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='noticia',
            name='estado',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='noticia',
            name='prioridad',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='perfil',
            name='tipo',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='cuerpo',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='estado',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='tipo',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='ruta',
            name='descripcion',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='ruta',
            name='dificultad',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='ruta',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='ruta',
            name='urlMap',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='salida',
            name='estado',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='salida',
            name='lugarEncuentro',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='celular',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='fonoEmergencia',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='acceso',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='faq',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salida',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellidos',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contactoEmergencia',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='derivarA',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='psw',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(default='', max_length=10),
        ),
    ]
