# Generated by Django 4.0.6 on 2022-10-02 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_centerlocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='townsmodel',
            name='County',
        ),
    ]