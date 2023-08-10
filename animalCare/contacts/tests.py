from django.test import TestCase
from django.urls import reverse


class ContactFormViewTest(TestCase):
    def test_contact_form_view_form_submission(self):
        url = reverse('contact form')

        response = self.client.post(url, {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'theme': 'Inquiry',
            'description': 'This is an inquiry.',
        })

        self.assertRedirects(response, reverse('home page'))

    def test_contact_form_view_get_request(self):
        url = reverse('contact form')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'contacts/contact_form.html')
