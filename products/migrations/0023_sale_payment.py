# Generated by Django 3.2.5 on 2021-09-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20210903_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='payment',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]