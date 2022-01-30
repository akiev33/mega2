# Generated by Django 4.0.1 on 2022-01-27 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('product', '0003_alter_product_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
