from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from users.models import Profile


def index(request):
    return render(request, 'main/index.html')


def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=user)
    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'main/user_profile.html', context)
