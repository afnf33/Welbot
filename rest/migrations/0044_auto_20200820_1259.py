# Generated by Django 3.0.8 on 2020-08-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0043_auto_20200820_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy_lecture',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]