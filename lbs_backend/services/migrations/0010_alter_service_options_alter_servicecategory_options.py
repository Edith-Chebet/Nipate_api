# Generated by Django 4.0.6 on 2022-10-03 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_rename_product_service_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Services', 'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='servicecategory',
            options={'verbose_name': 'Service Categories', 'verbose_name_plural': 'Service Categories'},
        ),
    ]
