# Generated by Django 3.1 on 2020-09-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0003_auto_20200925_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangm',
            name='harga_jual',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
