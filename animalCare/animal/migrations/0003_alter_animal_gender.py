# Generated by Django 4.2.3 on 2023-07-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_alter_animal_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
