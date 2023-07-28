from django.contrib import admin

from animal.models import Animal, SavedAnimal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(SavedAnimal)
class AnimalAdmin(admin.ModelAdmin):
    pass
