# Generated by Django 4.1.3 on 2022-11-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0006_especialidad_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Reservado', 'Reservado'), ('Atendida', 'Atendida')], max_length=200, null=True),
        ),
    ]