# Generated by Django 5.1.1 on 2024-09-18 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='measured_at',
            new_name='create_at',
        ),
    ]
