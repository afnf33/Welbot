# Generated by Django 3.0.8 on 2020-08-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0021_auto_20200819_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]