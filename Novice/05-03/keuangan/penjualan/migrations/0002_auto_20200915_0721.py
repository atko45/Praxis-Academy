# Generated by Django 3.1 on 2020-09-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjualan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjualan',
            name='tanggal',
            field=models.DateField(auto_now_add=True),
        ),
    ]
