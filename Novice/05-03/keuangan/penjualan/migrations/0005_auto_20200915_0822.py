# Generated by Django 3.1 on 2020-09-15 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjualan', '0004_auto_20200915_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjualan',
            name='tanggal',
            field=models.DateField(),
        ),
    ]