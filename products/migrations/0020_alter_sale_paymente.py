# Generated by Django 3.2.5 on 2021-09-03 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20210903_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='paymente',
            field=models.CharField(max_length=100),
        ),
    ]
