# Generated by Django 2.2 on 2020-09-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0004_auto_20200902_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='personil',
        ),
        migrations.RemoveField(
            model_name='band',
            name='posisi',
        ),
        migrations.AddField(
            model_name='band',
            name='label',
            field=models.TextField(default='(Label)'),
        ),
        migrations.AddField(
            model_name='band',
            name='tahun',
            field=models.TextField(default='(Tahun)'),
        ),
    ]
