# Generated by Django 3.0.8 on 2020-08-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0009_auto_20200818_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senior_center',
            name='tel',
            field=models.CharField(max_length=25),
        ),
    ]
