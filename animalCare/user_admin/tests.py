from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from contacts.models import Contact


class MarkContactAnsweredViewTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            theme='Inquiry',
            description='Test inquiry',
        )

    def test_mark_contact_answered_view(self):
        self.assertFalse(self.contact.is_answered)

        url = reverse('mark inquiries answered', args=[self.contact.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('unanswered inquiries'))

        self.contact.refresh_from_db()

        self.assertTrue(self.contact.is_answered)
