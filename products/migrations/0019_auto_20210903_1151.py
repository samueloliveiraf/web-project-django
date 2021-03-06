# Generated by Django 3.2.5 on 2021-09-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_sale_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ('time',)},
        ),
        migrations.AddField(
            model_name='sale',
            name='paymente',
            field=models.CharField(choices=[('CC', 'Cartao de Credido'), ('CD', 'Cartao de Debito'), ('DD', 'Dinheiro')], default=1, max_length=2, verbose_name='Forma Pagamento'),
            preserve_default=False,
        ),
    ]
