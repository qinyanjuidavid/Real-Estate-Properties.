# Generated by Django 2.2.8 on 2019-12-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_dashboard_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='sold',
        ),
        migrations.AddField(
            model_name='house',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
