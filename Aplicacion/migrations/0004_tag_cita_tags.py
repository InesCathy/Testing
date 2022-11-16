# Generated by Django 4.1.3 on 2022-11-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0003_cita_especialidad_cita_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='tags',
            field=models.ManyToManyField(to='Aplicacion.tag'),
        ),
    ]