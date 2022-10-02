# Generated by Django 4.0.6 on 2022-10-02 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_delete_townsmodel'),
        ('provider', '0003_remove_providerservice_locationid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='providermodel',
            name='CountyID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_county', to='locations.countymodel'),
        ),
    ]
