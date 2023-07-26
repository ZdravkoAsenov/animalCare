from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from profiles.models import CustomUser, ProfileModel


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}), label='Type password:')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}), label='Retype password:')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class EditProfileForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        exclude = ['profile']


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = []

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

