# Generated by Django 3.1 on 2020-09-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0009_utangm_dibayar'),
    ]

    operations = [
        migrations.AddField(
            model_name='penjualan3m',
            name='terima',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pem_kreditm',
            name='jumlah',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pem_lainm',
            name='dibayar',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pem_lainm',
            name='utang',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pem_tunaim',
            name='jumlah',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pembayaran_biayam',
            name='dibayar',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pembayaran_lainm',
            name='dibayar',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pembayaran_lainm',
            name='utang',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pend_lainm',
            name='jumlah',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='utangm',
            name='dibayar',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='utangm',
            name='jumlah',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]