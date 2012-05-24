# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.management import execute_manager
import settings

def syncdb(request):
	execute_manager(settings, ['manage.py','syncdb','--noinput'])
	return HttpResponseRedirect('/')
