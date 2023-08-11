from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model, get_user
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


class ProfileDeleteViewTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='User')
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_profile_delete_view(self):
        url = reverse('delete profile')

        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home page'))

        self.assertFalse(
            get_user_model().objects.filter(pk=self.user.pk).exists()
        )


class LogoutViewTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='User')
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_logout_view(self):
        # URL to the logout view
        url = reverse('logout')

        # Simulate accessing the logout view
        response = self.client.get(url)

        # Check that the response redirects as expected
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home page'))

        # Check that the user is logged out
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)