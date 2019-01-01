from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Story, Chapter, Character


class IndexView(generic.ListView):
    template_name = 'works/index.html'
    context_object_name = 'stories_list'

    def get_queryset(self):
        return Story.objects.order_by('-created_date')


# need to be removed later
def index(request):
    stories_list = Story.objects.order_by('-created_date')
    context = {
        'stories_list': stories_list
    }
    return render(request, 'works/index.html', context)


class StoryView(generic.DetailView):
    model = Story
    template_name = 'works/get_story.html'


# need to be removed later
def get_story(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    context = {
        'story': story
    }
    return render(request, 'works/get_story.html', context)


def get_chapter(request, story_id, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    context = {
        'chapter': chapter
    }
    return render(request, 'works/get_chapter.html', context)


def get_character(request, story_id, character_id):
    character = get_object_or_404(Character, pk=character_id)
    context = {
        'character': character
    }
    return render(request, 'works/get_character.html', context)
