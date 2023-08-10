from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from profiles.models import ProfileModel, CustomUser


class ProfileCreateViewTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='User')

    def test_profile_create_view(self):
        userModel = get_user_model()
        user = userModel.objects.create_user(username='testuser', password='testpassword')

        self.client.logout()

        self.assertTrue(self.client.login(username='testuser', password='testpassword'))

        self.assertEqual(get_user_model().objects.count(), 1)


class CustomLoginViewTest(TestCase):
    def setUp(self):
        userModel = get_user_model()
        self.group = Group.objects.create(name='User')
        self.user = userModel.objects.create_user(username='testuser', password='testpassword')

    def test_login_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        url = reverse('login')

        response = self.client.get(url)

        self.assertRedirects(response, reverse('home page'))

    def test_login_view_not_authenticated_user(self):
        self.client.logout()

        url = reverse('login')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'profiles/login.html')
