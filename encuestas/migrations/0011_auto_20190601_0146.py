# Generated by Django 2.2.1 on 2019-05-31 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0010_pacientes_id_android'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuestas',
            name='contestacion',
            field=models.TextField(blank=True, default='NO', null=True, verbose_name='SI o NO contestación'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='nombre',
            field=models.CharField(default='Complete los campos..', max_length=50, verbose_name='Nombre del Paciente'),
        ),
    ]
