# Generated by Django 2.1.3 on 2018-11-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_competicion_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='competicion',
            name='nombre',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
