# Generated by Django 4.1.3 on 2022-11-04 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='t_yil',
            field=models.DateField(),
        ),
    ]
