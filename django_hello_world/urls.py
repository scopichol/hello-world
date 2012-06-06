from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_hello_world.hello.views.home', name='home'),
    url(r'^profile/', include('django_hello_world.accounts.urls')),
    url(r'^uploadprogress$', 'django_hello_world.jquerywidgets.views.get_upload_progress', name='uploadprogress'),
    url(r'^syncdb$', 'django_hello_world.hello.views.syncdb', name='syncdb'),
    url(r'^resetaccounts$', 'django_hello_world.hello.views.reset_accounts', name='reset_accounts'),
    url(r'^log$', 'django_hello_world.hello.views.requestlog', name='requestlog'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # url(r'^django_hello_world/', include('django_hello_world.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
