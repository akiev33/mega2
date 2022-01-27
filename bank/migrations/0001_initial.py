# Generated by Django 4.0.1 on 2022-01-27 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_account',
            fields=[
                ('money', models.PositiveIntegerField()),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='company.company')),
            ],
        ),
    ]