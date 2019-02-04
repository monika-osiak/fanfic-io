from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .forms import SignUpForm
from .models import Profile


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def sign_up(request):
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            '''new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']'''
            new_user.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=form.cleaned_data['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('works:index'))

    context = {'form': form}
    return render(request, 'users/sign_up.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=user)
    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'users/user_profile.html', context)
