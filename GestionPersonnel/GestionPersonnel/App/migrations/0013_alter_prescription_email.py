# Generated by Django 4.2.6 on 2023-12-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_prescription_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]