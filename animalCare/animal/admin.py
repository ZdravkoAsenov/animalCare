from django.contrib import admin

from animal.models import Animal, SavedAnimal, MedicalExamination


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(SavedAnimal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(MedicalExamination)
class AnimalAdmin(admin.ModelAdmin):
    pass
