# Generated by Django 5.0.3 on 2024-04-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_cliente_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='hijos',
            field=models.IntegerField(null=True),
        ),
    ]
