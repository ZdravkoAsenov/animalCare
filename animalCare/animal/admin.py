from django.contrib import admin

from animal.models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass