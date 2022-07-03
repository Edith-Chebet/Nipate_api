# Generated by Django 3.2.12 on 2022-07-03 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_alter_townsmodel_county'),
        ('users', '0002_alter_customuser_idnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='LocationID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.townsmodel'),
        ),
    ]
