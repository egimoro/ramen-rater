# Generated by Django 2.2.5 on 2019-09-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramen_rater', '0008_auto_20190922_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ramen',
            name='daterate',
            field=models.DateField(),
        ),
    ]