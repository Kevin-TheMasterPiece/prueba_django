# Generated by Django 5.0.3 on 2024-04-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(max_length=10),
        ),
    ]
