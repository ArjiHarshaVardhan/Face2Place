# Generated by Django 4.1.6 on 2023-04-16 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_passengers_delete_pad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='passenger',
        ),
    ]
