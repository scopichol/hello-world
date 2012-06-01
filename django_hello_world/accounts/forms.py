from django.forms import ModelForm, HiddenInput
from django.contrib.auth.models import User
from models import UserProfile
from django_hello_world.jquerywidgets.widgets import CalendarWidget
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
            'user':HiddenInput,
            'birthday':CalendarWidget,
        }
