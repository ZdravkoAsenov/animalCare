from django import forms
from django.contrib.auth.models import Group


class ChangeUserGroupForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all())