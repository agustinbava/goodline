# Generated by Django 4.1.7 on 2023-03-12 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_remove_pregunta_fecha_respuesta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='tipo_pregunta',
            field=models.CharField(choices=[('Texto', 'Texto'), ('Multiples', 'Multiples'), ('Unico', 'Unico')], max_length=100),
        ),
    ]
