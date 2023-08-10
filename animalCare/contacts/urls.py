from django.urls import path

from contacts.views import contact_form_view

urlpatterns = [
    path('', contact_form_view, name='contact form'),
]