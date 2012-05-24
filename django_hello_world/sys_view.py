# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.management import execute_manager
import django_hello_world.settings

def syncdb(request):
	execute_manager(django_hello_world.settings, ['manage.py','syncdb','--noinput'])
	return HttpResponseRedirect('/')
