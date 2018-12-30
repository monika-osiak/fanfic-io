from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('MY VERY FIRST VIEW IN THIS APP, WOOOOOOOOOOOOOOAH!!!')
