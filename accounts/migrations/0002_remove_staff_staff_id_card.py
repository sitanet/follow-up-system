# Generated by Django 4.2.1 on 2023-06-03 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='staff_id_card',
        ),
    ]
