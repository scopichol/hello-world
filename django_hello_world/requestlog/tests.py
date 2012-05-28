from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client
from models import RequestLog

class RequestlogTest(TestCase):
    def test_model(self):
        RequestLog.objects.count()
        
    def test_middleware(self):
        count = RequestLog.objects.count()
        c = Client()
        response = c.get(reverse('home'))
        newCount = RequestLog.objects.count()
        self.assertEqual(count+1, newCount)
        
    def test_context_settings(self):
        c = Client()
        response = c.get(reverse('home'))
        hasSettings = False
        for context in response.context[0]:
            if context.has_key('settings'):
                hasSettings = True
        self.assertTrue(hasSettings)
