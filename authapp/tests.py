from django.test import TestCase

# Create your tests here.
def test_activate_account_view_get_method(self):
        response = self.client.get('/auth/activate/12345678901234567890123456789012/12345678901234567890123456789012')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'activate.html')

def test_activate_account_view_post_method(self):
        response = self.client.post('/auth/activate/12345678901234567890123456789012/12345678901234567890123456789012', data={})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/auth/login/')
        self.assertEqual(len(mail.outbox), 1)