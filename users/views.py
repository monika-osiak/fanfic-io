from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction

from .forms import SignUpForm, UserForm, ProfileForm, UsernameChangeForm
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
    displayed_user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=displayed_user)
    user_works_list = displayed_user.story_set.all()[:3]
    user_bookmarks_list = user_profile.bookmarks.all()[:3]
    context = {
        'displayed_user': displayed_user,
        'user_profile': user_profile,
        'user_works_list': user_works_list,
        'user_bookmarks_list': user_bookmarks_list,
        'owner': displayed_user == request.user
    }
    return render(request, 'users/profile.html', context)


def works(request, username):
    author = get_object_or_404(User, username=username)
    works_list = author.story_set.all()
    context = {
        'author': author,
        'works_list': works_list,
    }
    return render(request, 'users/works.html', context)


# TODO: drafts view
def drafts(request, username):
    return HttpResponse('List of unposted works written by ' + username)


def bookmarks(request, username):
    owner = get_object_or_404(User, username=username)
    bookmarks_list = owner.profile.bookmarks.all()
    context = {
        'owner': owner,
        'bookmarks': bookmarks_list
    }
    return render(request, 'users/bookmarks.html', context)


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
    user = get_object_or_404(User, username=username)
    if user != request.user:
        raise Http404
    if request.method != 'POST':
        change_username_form = UsernameChangeForm(instance=user)
    else:
        change_username_form = UsernameChangeForm(request.POST, instance=user)
        if change_username_form.is_valid():
            change_username_form.save()
            return HttpResponseRedirect(reverse('users:profile', args=[user.username]))
    context = {
        'user': user,
        'form': change_username_form
    }
    return render(request, 'users/change_username.html', context)


# TODO: change_password view
def change_password(request, username):
    return HttpResponse('Change your password ' + username + ' (just not yet, okay?)')


# TODO: change_email view
def change_email(request, username):
    return HttpResponse('Change your email ' + username + ' (just not yet, okay?)')
