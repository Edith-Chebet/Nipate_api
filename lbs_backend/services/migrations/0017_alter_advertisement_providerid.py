# Generated by Django 4.0.6 on 2022-10-28 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0016_remove_advertisement_userid_advertisement_providerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='ProviderID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
