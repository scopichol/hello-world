from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField(verbose_name="Date of birth", null=True, blank=True)
    bio = models.TextField(verbose_name="Biography", null=True, blank=True)
    jabber = models.EmailField(verbose_name="Jabber", null=True, blank=True)
    skype = models.CharField(max_length=75, verbose_name="Skype", null=True, blank=True)
    otherContacts = models.TextField(verbose_name="Other contacts", null=True, blank=True)
    photo = models.ImageField(upload_to='profile', verbose_name="Photo", null=True, blank=True)
    