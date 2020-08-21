# Generated by Django 3.0.8 on 2020-08-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0029_auto_20200819_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='culture_event',
            name='date',
        ),
        migrations.AddField(
            model_name='culture_event',
            name='enddate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='culture_event',
            name='startdate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
