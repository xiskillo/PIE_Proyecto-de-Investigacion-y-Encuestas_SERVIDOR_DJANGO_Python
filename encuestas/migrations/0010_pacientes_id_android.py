# Generated by Django 2.2.1 on 2019-05-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0009_auto_20190525_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='id_android',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Identificado Android para Push'),
        ),
    ]
