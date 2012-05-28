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
