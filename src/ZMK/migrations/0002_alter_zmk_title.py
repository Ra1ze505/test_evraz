# Generated by Django 4.0.5 on 2022-06-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZMK', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zmk',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
