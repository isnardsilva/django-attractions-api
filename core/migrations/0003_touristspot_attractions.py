# Generated by Django 3.0.7 on 2020-06-13 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
        ('core', '0002_auto_20200613_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='attractions',
            field=models.ManyToManyField(to='attractions.Attraction'),
        ),
    ]
