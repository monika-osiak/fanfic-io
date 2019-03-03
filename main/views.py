from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

# TODO: main/index.html -> base
# TODO: fix all the templates
# TODO: remove my css
# TODO: MAKE EVERYTHING PRETTY!!!
