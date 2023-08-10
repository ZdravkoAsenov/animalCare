from django.contrib import admin

from animal.models import Animal, SavedAnimal, MedicalExamination


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed']
    search_fields = ['name', 'species', 'breed']
    list_per_page = 10
    list_filter = ['name', 'species', 'breed']


@admin.register(SavedAnimal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['user', 'animal', 'review_date', 'review_hour']
    search_fields = ['user', 'animal']
    list_filter = ['review_date', 'review_hour']
    list_per_page = 10


@admin.register(MedicalExamination)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['user', 'animal', 'date']
    list_filter = ['date']
    search_fields = ['user', 'animal']
    list_per_page = 10
