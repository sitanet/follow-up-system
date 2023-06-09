# Generated by Django 4.2.2 on 2023-06-15 14:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('first_name', models.CharField(max_length=50, unique=True)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('date_of_birth', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('email', models.EmailField(blank=True, max_length=40, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.PositiveIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True)),
                ('marital_status', models.PositiveIntegerField(blank=True, choices=[(1, 'Single'), (2, 'Married')], null=True)),
                ('occupation', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('nationality', models.CharField(blank=True, max_length=20, null=True)),
                ('kcc_center', models.CharField(blank=True, max_length=20, null=True)),
                ('wedding_ann', models.CharField(blank=True, max_length=30, null=True)),
                ('join', models.CharField(blank=True, max_length=20, null=True)),
                ('reg_date', models.CharField(blank=True, max_length=20, null=True)),
                ('about', models.CharField(blank=True, max_length=20, null=True)),
                ('dept', models.CharField(blank=True, max_length=20, null=True)),
                ('purpose', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('team_sup', models.CharField(blank=True, max_length=20, null=True)),
                ('date_created', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('comment', models.TextField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='follow_up.member')),
            ],
        ),
    ]
