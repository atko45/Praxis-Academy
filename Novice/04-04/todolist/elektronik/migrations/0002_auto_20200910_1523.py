# Generated by Django 2.2 on 2020-09-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elektronik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elektronik',
            name='elek_image',
            field=models.CharField(default='Image', max_length=255),
        ),
        migrations.AlterField(
            model_name='elektronik',
            name='elek_info',
            field=models.CharField(default='Info', max_length=255),
        ),
        migrations.AlterField(
            model_name='elektronik',
            name='elek_name',
            field=models.CharField(default='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='elektronik',
            name='elek_price',
            field=models.CharField(default='Gambar', max_length=255),
        ),
        migrations.AlterField(
            model_name='elektronik',
            name='elek_stock',
            field=models.CharField(default='Stock', max_length=255),
        ),
    ]
