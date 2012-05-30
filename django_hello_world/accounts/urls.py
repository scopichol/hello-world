from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns('',
    url(r'^edit$', views.editProfile, name='editprofile'),
)
