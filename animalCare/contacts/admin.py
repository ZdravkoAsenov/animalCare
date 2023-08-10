from django.contrib import admin

from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'theme', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'theme']
    list_filter = ['created_at']
    ordering = ['-created_at']
    list_per_page = 10
