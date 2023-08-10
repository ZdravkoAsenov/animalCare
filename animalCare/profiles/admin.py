from django.contrib import admin

from profiles.models import ProfileModel, CustomUser


@admin.register(ProfileModel)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'gender']
    search_fields = ['first_name', 'last_name']
    list_filter = ['age', 'gender']
    list_per_page = 10

    def get_username(self, obj):
        return obj.profile.username

    get_username.short_description = 'Username'


@admin.register(CustomUser)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ['username', 'email']
    list_per_page = 10
