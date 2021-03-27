# Generated by Django 3.1.7 on 2021-03-22 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('text', models.TextField(max_length=300, verbose_name='text')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('password', models.CharField(max_length=8, verbose_name='password')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
        ),
    ]
