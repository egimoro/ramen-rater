# Generated by Django 2.2.3 on 2019-09-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ramen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('variety', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=7)),
                ('country', models.CharField(max_length=70)),
                ('daterate', models.DateTimeField(verbose_name='date rated')),
                ('stars', models.FloatField()),
            ],
        ),
    ]
