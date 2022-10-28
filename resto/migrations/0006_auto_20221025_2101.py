# Generated by Django 4.1 on 2022-10-25 14:01

from django.db import migrations
from django.db import migrations, models
import uuid



class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0005_auto_20221025_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='resto_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, serialize=False),
        ),
    ]