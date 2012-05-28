"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client



class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class HttpTest(TestCase):
    def test_home(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My profile info!')
        
    def test_context_settings(self):
        c = Client()
        response = c.get(reverse('home'))
        hasSettings = False
        for context in response.context[0]:
            if context.has_key('settings'):
                hasSettings = True
        self.assertTrue(hasSettings)
        

class RequestlogTest(TestCase):
    def test_link(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'requests')
        
    def test_urlresolving(self):
        reverse('requestlog')
        
    def test_view(self):
        c = Client()
        response = c.get(reverse('requestlog'))
        hasObject_list = False
        for context in response.context[0]:
            if context.has_key('object_list'):
                hasObject_list = True
        self.assertTrue(hasObject_list)
