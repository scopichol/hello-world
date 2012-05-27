from annoying.decorators import render_to
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.management import execute_manager
from django_hello_world import settings
from django_hello_world.requestlog.models import RequestLog

@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()
    try:
        myself = User.objects.get(id=2)
    except:
        myself = None
    return {'users': users, 'myself':myself}


def syncdb(request):
	execute_manager(settings, ['manage.py','syncdb','--noinput'])
	return HttpResponseRedirect('/')

@render_to('hello/requestlog.html')
def requestlog(request):
    logEntries = RequestLog.objects.all().order_by('id')[:10]
    return {'object_list': logEntries}
