# Generated by Django 4.2.1 on 2024-01-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0026_alter_consultation_service_alter_consultation_sexe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponibilite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medecin', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
            ],
        ),
    ]
