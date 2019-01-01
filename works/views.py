from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Story, Chapter, Character


class IndexView(generic.ListView):
    template_name = 'works/index.html'
    context_object_name = 'stories_list'

    def get_queryset(self):
        return Story.objects.order_by('-created_date')


class StoryView(generic.DetailView):
    model = Story
    template_name = 'works/get_story.html'


class ChapterView(generic.DetailView):
    model = Chapter
    template_name = 'works/get_chapter.html'


class CharacterView(generic.DetailView):
    model = Character
    template_name = 'works/get_character.html'