# Generated by Django 3.2.5 on 2021-07-31 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(default=16, max_length=255),
            preserve_default=False,
        ),
    ]
