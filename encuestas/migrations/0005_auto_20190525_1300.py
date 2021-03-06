# Generated by Django 2.2.1 on 2019-05-25 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0004_auto_20190522_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuestas',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuestas.Pacientes', to_field='nuhsa', verbose_name='Paciente'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='nuhsa',
            field=models.CharField(max_length=15, unique=True, verbose_name='NUHSA'),
        ),
    ]
