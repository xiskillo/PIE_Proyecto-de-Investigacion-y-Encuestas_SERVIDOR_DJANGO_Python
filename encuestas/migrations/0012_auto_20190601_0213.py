# Generated by Django 2.2.1 on 2019-06-01 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0011_auto_20190601_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuestas',
            name='respuesta',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Respuesta a la Pregunta'),
        ),
    ]