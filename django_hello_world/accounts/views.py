from annoying.decorators import render_to
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django_hello_world.accounts.forms import UserProfileForm, UserForm

@render_to('accounts/editprofile.html')
def editProfile(request):
    myself = User.objects.get(id=2)
    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=myself)
        profileForm = UserProfileForm(request.POST, request.FILES, instance=myself.get_profile())
        print 'userForm', userForm.is_valid()
        print 'profileForm', profileForm.is_valid()
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            return HttpResponseRedirect('/')
    else:
        userForm = UserForm(instance=myself)
        profileForm = UserProfileForm(instance=myself.get_profile())
        
    return {'userForm': userForm, 'profileForm': profileForm, 'myself':myself}
