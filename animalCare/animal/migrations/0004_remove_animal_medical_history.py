# Generated by Django 4.2.3 on 2023-07-21 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0003_alter_animal_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='medical_history',
        ),
    ]
