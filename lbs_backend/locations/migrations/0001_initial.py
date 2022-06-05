# Generated by Django 3.2.12 on 2022-06-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Counties',
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='TownsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Towns',
                'verbose_name_plural': 'Towns',
            },
        ),
    ]
