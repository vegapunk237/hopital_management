# Generated by Django 4.2.6 on 2023-12-27 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0019_alter_prescription_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]