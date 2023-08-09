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

    def __str__(self):
        return self.name


class SavedAnimal(models.Model):
    class ReviewType(models.TextChoices):
        PRIMARY_EXAMINATION = 'Primary examination', 'Primary examination'
        CASTRATION = 'Castration', 'Castration'
        VACCINATION = 'Vaccination', 'Vaccination'
        DEWORMING = 'Deworming', 'Deworming'

    user = models.ForeignKey(userModel, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    review_date = models.DateField()
    review_hour = models.IntegerField(choices=[(hour, hour) for hour in range(9, 19) if hour != 12])
    review_type = models.CharField(
        max_length=30,
        choices=ReviewType.choices,
        default=ReviewType.PRIMARY_EXAMINATION,
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'animal', 'review_hour')


class MedicalExamination(models.Model):
    user = models.ForeignKey(userModel, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        formatted_date = self.date.strftime("%Y-%m-%d")
        return f"{self.animal.name} - {formatted_date}"

    def save(self, *args, **kwargs):
        saved_animal = SavedAnimal.objects.filter(user=self.user, animal=self.animal).first()
        if saved_animal:
            saved_animal.delete()
        super(MedicalExamination, self).save(*args, **kwargs)
