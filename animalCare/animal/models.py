from django.contrib.auth import get_user_model
from django.db import models

userModel = get_user_model()


class Animal(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.ForeignKey(userModel, on_delete=models.CASCADE)


class SavedAnimal(models.Model):
    user = models.ForeignKey(userModel, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    review_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'animal')
