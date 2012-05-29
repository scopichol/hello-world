from django.forms import ModelForm
from django.contrib.auth.models import User
from models import UserProfile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
