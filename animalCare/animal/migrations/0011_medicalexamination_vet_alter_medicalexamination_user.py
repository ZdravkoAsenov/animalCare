# Generated by Django 4.2.3 on 2023-08-01 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animal', '0010_medicalexamination'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalexamination',
            name='vet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='examinations_as_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicalexamination',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
