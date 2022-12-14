# Generated by Django 4.1.3 on 2022-11-10 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creada', models.DateTimeField(auto_now_add=True, null=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Reservado', 'Reservado'), ('Atendido', 'Atendido')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('precio', models.FloatField(null=True)),
                ('categoria', models.CharField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=200, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_creada', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
