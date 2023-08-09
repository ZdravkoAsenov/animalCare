from django.contrib import admin

from profiles.models import ProfileModel, CustomUser


@admin.register(ProfileModel)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'get_username']

    def get_username(self, obj):
        return obj.profile.username

    get_username.short_description = 'Username'


@admin.register(CustomUser)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
