# Generated by Django 3.2.5 on 2021-09-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_sale_paymente'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='paymente',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
