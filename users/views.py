from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction

from .forms import SignUpForm, UserForm, ProfileForm
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
    user_works_list = user.story_set.all()[:3]
    context = {
        'user': user,
        'user_profile': user_profile,
        'user_works_list': user_works_list
    }
    # TODO: maybe add some recent bookmarks?
    return render(request, 'users/profile.html', context)


# TODO: works view
def works(request, username):
    return HttpResponse('List of works written by ' + username)


# TODO: drafts view
def drafts(request, username):
    return HttpResponse('List of unposted works written by ' + username)


# TODO: bookmarks view
def bookmarks(request, username):
    return HttpResponse('List of stories bookmarked by ' + username)


@login_required
@transaction.atomic
def edit(request, username):
    user = get_object_or_404(User, username=username)
    if user != request.user:
        raise Http404
    if request.method != 'POST':
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)
    else:
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('users:profile', args=[username]))
    context = {
        'user': user,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/edit.html', context)


# TODO: change_username view
def change_username(request, username):
    return HttpResponse('Change your username ' + username + ' (just not yet, okay?)')


# TODO: change_password view
def change_password(request, username):
    return HttpResponse('Change your password ' + username + ' (just not yet, okay?)')


# TODO: change_email view
def change_email(request, username):
    return HttpResponse('Change your email ' + username + ' (just not yet, okay?)')
