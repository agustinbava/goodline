# Generated by Django 4.1.7 on 2023-03-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0010_alter_user_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='edad',
            field=models.IntegerField(default=None),
        ),
    ]