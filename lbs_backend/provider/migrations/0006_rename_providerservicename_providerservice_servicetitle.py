# Generated by Django 4.0.6 on 2022-10-13 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_providerservice_servicedescription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='providerservice',
            old_name='ProviderServiceName',
            new_name='ServiceTitle',
        ),
    ]
