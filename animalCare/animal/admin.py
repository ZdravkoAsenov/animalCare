from django.contrib import admin

from animal.models import Animal, SavedAnimal, MedicalExamination


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed']


@admin.register(SavedAnimal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['user', 'animal', 'review_date', 'review_hour']


@admin.register(MedicalExamination)
class AnimalAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'animal']
