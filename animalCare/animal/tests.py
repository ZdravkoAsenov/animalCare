from datetime import date
from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from animal.forms import DeleteAnimalForm
from animal.models import Animal, SavedAnimal


class AnimalListViewTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='User')
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_animal_list_view_with_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        Animal.objects.create(name='Fluffy', species='Cat', owner=self.user, age=10, gender='Male', weight=5)

        url = reverse('list animal')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'animal/animal_list.html')

        animals_in_context = response.context['object_list']
        self.assertEqual(animals_in_context.count(), 1)
        self.assertEqual(animals_in_context[0].name, 'Fluffy')
        self.assertEqual(animals_in_context[0].species, 'Cat')
        self.assertEqual(animals_in_context[0].age, 10)


class CreateAnimalViewTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='User')
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_animal_view(self):
        url = reverse('create animal')

        response = self.client.post(url, {
            'name': 'Fluffy',
            'species': 'Cat',
            'age': 10,
            'owner': self.user,
            'breed': 'cat',
            'gender': 'Male',
            'weight': 5
        })

        self.assertTrue(Animal.objects.filter(name='Fluffy').exists())


class AnimalSaveHourViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.group = Group.objects.create(name='User')
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.animal = Animal.objects.create(name='Fluffy', species='Cat', owner=self.user, age=10, gender='Male',
                                            weight=5)

    def test_animal_save_hour_view_get(self):
        url = reverse('save hour animal', args=[self.animal.pk])

        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/record_animal_hour.html')


class DeleteAnimalFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.group = Group.objects.create(name='User')
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.animal = Animal.objects.create(name='Fluffy', species='Cat', owner=self.user, age=10, gender='Male',
                                            weight=5)

    def test_delete_animal_form(self):
        form = DeleteAnimalForm(instance=self.animal)
        self.client.login(username='testuser', password='testpassword')

        self.assertEqual(form.is_valid(), False)

        response = self.client.post(reverse('delete animal', args=[self.animal.pk]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Animal.objects.filter(pk=self.animal.pk).exists())

        form = DeleteAnimalForm(instance=self.animal)
        form.save(commit=True)
        self.assertFalse(Animal.objects.filter(pk=self.animal.pk).exists())
