# Generated by Django 4.0.6 on 2022-10-02 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_rename_product_service_and_more'),
        ('locations', '0004_remove_townsmodel_county'),
        ('provider', '0003_remove_providerservice_locationid_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TownsModel',
        ),
    ]
