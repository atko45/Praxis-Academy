# Generated by Django 2.2 on 2020-10-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notif', '0002_auto_20201014_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datanotif',
            name='tanggal_jatuh_tempo',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='datanotif',
            name='tanggal_pinjam',
            field=models.DateField(auto_now_add=True),
        ),
    ]
