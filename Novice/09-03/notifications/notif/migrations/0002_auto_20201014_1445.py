# Generated by Django 2.2 on 2020-10-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notif', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datanotif',
            name='tanggal_pinjam',
            field=models.DateField(),
        ),
    ]