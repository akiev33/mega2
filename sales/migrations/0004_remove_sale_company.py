# Generated by Django 4.0.1 on 2022-01-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_sale_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='company',
        ),
    ]
