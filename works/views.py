from django.shortcuts import render
from django.http import HttpResponse

from .models import Story, Chapter, Character


def index(request):
    stories_list = Story.objects.order_by('-created_date')
    context = {
        'stories_list': stories_list
    }
    return render(request, 'works/index.html', context)


def get_story(request, story_id):
    return HttpResponse('You are watching the story number %s' % story_id)


def get_chapters(request, story_id):
    return HttpResponse('You are watching chapters of the story number %s' % story_id)


def get_chapter(request, story_id, chapter_id):
    return HttpResponse('You are watching the chapter %s of the story number %s' % (chapter_id, story_id))


def get_characters(request, story_id):
    return HttpResponse('You are watching characters of the story number %s' % story_id)
