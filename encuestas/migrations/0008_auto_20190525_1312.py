# Generated by Django 2.2.1 on 2019-05-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0007_auto_20190525_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='nombre',
            field=models.CharField(default='EDITE EL NOMBRE', max_length=50, verbose_name='Nombre del Paciente'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='nuhsa',
            field=models.CharField(max_length=20, unique=True, verbose_name='NUHSA'),
        ),
    ]
