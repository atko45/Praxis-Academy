# Generated by Django 3.1 on 2020-09-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0007_penjualan2m_diterima'),
    ]

    operations = [
        migrations.CreateModel(
            name='saldom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_awal', models.IntegerField(default='')),
            ],
        ),
    ]
