# Generated by Django 2.2 on 2020-08-21 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.TextField(default='pending'),
        ),
    ]
