# Generated by Django 2.2 on 2020-10-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notif', '0006_auto_20201022_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datanotif',
            name='tanggal_jatuh_tempo',
            field=models.IntegerField(default=0),
        ),
    ]
