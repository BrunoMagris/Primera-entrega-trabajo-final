# Generated by Django 4.1 on 2022-09-22 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nacimiento',
        ),
    ]
