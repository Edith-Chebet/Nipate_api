# Generated by Django 4.0.6 on 2022-10-26 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0008_alter_providerservice_options_and_more'),
        ('services', '0015_alter_advertisement_addescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='UserID',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='ProviderID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provider.providermodel'),
        ),
    ]
