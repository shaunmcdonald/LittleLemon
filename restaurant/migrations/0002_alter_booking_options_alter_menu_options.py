# Generated by Django 5.1.2 on 2024-11-01 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['booking_date', 'name']},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['title']},
        ),
    ]
