# Generated by Django 2.2 on 2020-09-04 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0005_auto_20200903_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='keterangan',
            name='aliran',
            field=models.TextField(default='(Aliran)'),
        ),
        migrations.AddField(
            model_name='keterangan',
            name='nama_band',
            field=models.TextField(default='(Nama Band)'),
        ),
        migrations.AddField(
            model_name='keterangan',
            name='negara_asal',
            field=models.TextField(default='(Negara Asal)'),
        ),
        migrations.AddField(
            model_name='keterangan',
            name='status',
            field=models.TextField(default='(Status)'),
        ),
        migrations.AlterField(
            model_name='keterangan',
            name='label',
            field=models.TextField(default='(Label)'),
        ),
        migrations.AlterField(
            model_name='keterangan',
            name='tahun',
            field=models.TextField(default='(Tahun)'),
        ),
    ]