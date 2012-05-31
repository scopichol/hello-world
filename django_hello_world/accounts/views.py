from annoying.decorators import render_to
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django_hello_world.accounts.forms import UserProfileForm, UserForm
from django.shortcuts import get_object_or_404
from models import UserProfile
from django.conf import settings

@render_to('accounts/editprofile.html')
def editProfile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        profile = user.get_profile()
    except:
        profile = UserProfile(user = user)

    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=user)
        profileForm = UserProfileForm(request.POST, request.FILES, instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            new_profile = profileForm.save(commit=False)
            new_profile.user = user
            new_profile.save()
            return HttpResponseRedirect('/')
    else:
        userForm = UserForm(instance=user)
        profileForm = UserProfileForm(instance=profile)
        
    return {'userForm': userForm, 'profileForm': profileForm}
