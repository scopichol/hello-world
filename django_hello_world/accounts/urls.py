from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns('',
    url(r'^(?P<user_id>\d+)/edit$', views.editProfile, name='editprofile'),
)
