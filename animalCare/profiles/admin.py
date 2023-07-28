from django.contrib import admin

from profiles.models import ProfileModel, CustomUser


@admin.register(ProfileModel)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomUser)
class AnimalAdmin(admin.ModelAdmin):
    pass
