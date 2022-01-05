# Generated by Django 4.0.1 on 2022-01-05 02:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolfees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalstudent',
            name='addreess',
            field=models.CharField(blank=True, help_text='Direccion de la casa', max_length=254, null=True, verbose_name='Direccion'),
        ),
        migrations.AddField(
            model_name='historicalstudent',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AddField(
            model_name='historicalstudent',
            name='phone',
            field=models.CharField(blank=True, help_text='Celular o Convencional', max_length=14, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'Se requiere un teléfono válido')], verbose_name='Telefono'),
        ),
        migrations.AddField(
            model_name='student',
            name='addreess',
            field=models.CharField(blank=True, help_text='Direccion de la casa', max_length=254, null=True, verbose_name='Direccion'),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, help_text='Celular o Convencional', max_length=14, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'Se requiere un teléfono válido')], verbose_name='Telefono'),
        ),
    ]
