from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client


class HttpTest(TestCase):
    def test_urlresolving(self):
        reverse('requestlog')
        
    def test_home(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'requests')
        
    def test_context_settings(self):
        c = Client()
        response = c.get(reverse('home'))
        hasSettings = False
        for context in response.context[0]:
            if context.has_key('settings'):
                hasSettings = True
        self.assertTrue(hasSettings)
