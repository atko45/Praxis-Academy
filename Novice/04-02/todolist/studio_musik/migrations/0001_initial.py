# Generated by Django 2.2 on 2020-09-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_label', models.CharField(default='(Nama Label)', max_length=255)),
                ('tahun_berdiri', models.CharField(default='(Tahun Berdiri)', max_length=255)),
                ('status_label', models.CharField(default='(Status Label)', max_length=255)),
            ],
        ),
    ]