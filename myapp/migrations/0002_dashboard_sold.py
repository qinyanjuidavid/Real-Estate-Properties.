# Generated by Django 2.2.8 on 2019-12-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
