# Generated by Django 3.1 on 2020-09-16 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barangm',
            options={'ordering': ['barang']},
        ),
    ]
