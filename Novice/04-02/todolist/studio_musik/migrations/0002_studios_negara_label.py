# Generated by Django 2.2 on 2020-09-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_musik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studios',
            name='negara_label',
            field=models.CharField(default='(Status Label)', max_length=255),
        ),
    ]