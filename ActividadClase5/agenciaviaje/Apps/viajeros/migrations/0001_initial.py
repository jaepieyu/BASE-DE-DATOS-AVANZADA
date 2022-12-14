# Generated by Django 4.1.1 on 2022-09-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viajeros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreViajeros', models.CharField(help_text='Ingrese el Nombre del Viajero', max_length=100)),
                ('direccionViajeros', models.CharField(help_text='Ingrese la Direccion del Viajero', max_length=100)),
                ('telefonoViajeros', models.CharField(help_text='Ingrese el Telefono del Viajero', max_length=12)),
            ],
            options={
                'verbose_name': 'viajero',
                'verbose_name_plural': 'viajeros',
            },
        ),
    ]
