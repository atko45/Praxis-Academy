# Generated by Django 3.1 on 2020-09-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0006_auto_20200916_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='penjualan2m',
            name='terima',
            field=models.IntegerField(default=0),
        ),
    ]