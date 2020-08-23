# Generated by Django 3.0.8 on 2020-08-19 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0040_auto_20200819_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Culture_genre',
            fields=[
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('available', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=20)),
                ('target', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('image', models.URLField()),
                ('starttime', models.CharField(max_length=10)),
                ('endtime', models.CharField(max_length=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rest.City')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rest.Culture_genre')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rest.Infrastructure')),
            ],
        ),
        migrations.CreateModel(
            name='Culture_Event',
            fields=[
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('target', models.CharField(max_length=50)),
                ('fare', models.CharField(max_length=300)),
                ('available', models.BooleanField(default=False)),
                ('url', models.URLField(max_length=300)),
                ('image', models.URLField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rest.Culture_genre')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rest.Infrastructure')),
            ],
        ),
    ]