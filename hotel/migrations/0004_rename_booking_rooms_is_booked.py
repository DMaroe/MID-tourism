# Generated by Django 4.1 on 2022-10-30 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_rooms_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms',
            old_name='booking',
            new_name='is_booked',
        ),
    ]
