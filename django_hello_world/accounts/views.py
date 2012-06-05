from annoying.decorators import render_to
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django_hello_world.accounts.forms import UserProfileForm, UserForm
from django.shortcuts import get_object_or_404
from models import UserProfile
from django.conf import settings
import json

@render_to('accounts/editprofile.html')
def editProfile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if not request.user.has_perm('accounts.change_userprofile') and user != request.user:
        return HttpResponseRedirect(settings.LOGIN_URL)
        
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

def editProfileAjax(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if not request.user.has_perm('accounts.change_userprofile') and user != request.user:
        return HttpResponseRedirect(settings.LOGIN_URL)
        
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
            result = 'success'
            response = userForm.cleaned_data
            response.update(profileForm.cleaned_data)
            del response['user']
            if response.has_key('photo'):
                response['photo'] = str(new_profile.photo)
            response['birthday'] = profileForm.fields['birthday'].widget._format_value(new_profile.birthday)
        else:
            result = 'error'
            response = userForm.errors.copy()
            response.update(profileForm.errors)
        return HttpResponse(json.dumps({'response':response, 'result':result}), mimetype='application/json')
    else:
        userForm = UserForm(instance=user)
        profileForm = UserProfileForm(instance=profile)
        return HttpResponse(json.dumps({'userForm':'userForm', 'profileForm':'profileForm'}))
    return {'userForm': userForm, 'profileForm': profileForm}
