# Generated by Django 2.2.8 on 2019-12-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20191226_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='contact_phone',
            field=models.CharField(default='0700215645', max_length=20),
        ),
    ]
