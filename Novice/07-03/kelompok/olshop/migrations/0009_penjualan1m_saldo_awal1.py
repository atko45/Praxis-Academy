# Generated by Django 2.2 on 2020-09-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0008_penjualan1m_saldo_awal'),
    ]

    operations = [
        migrations.AddField(
            model_name='penjualan1m',
            name='saldo_awal1',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]