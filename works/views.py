from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Story, Chapter, Character
from .forms import StoryForm, ChapterForm, CharacterForm


class IndexView(generic.ListView):
    template_name = 'works/index.html'
    context_object_name = 'stories_list'

    def get_queryset(self):
        return Story.objects.filter().order_by('-created_date')


class StoryView(generic.DetailView):
    model = Story
    template_name = 'works/get_story.html'


class ChapterView(generic.DetailView):
    model = Chapter
    template_name = 'works/get_chapter.html'


class CharacterView(generic.DetailView):
    model = Character
    template_name = 'works/get_character.html'


@login_required
def new_story(request):
    if request.method != 'POST':
        form = StoryForm()
    else:
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            return HttpResponseRedirect(reverse('works:index'))

    context = {
        'form': form
    }
    return render(request, 'works/new_story.html', context)

# TODO: user is able to add new character/chapter only to his own story

@login_required
def new_chapter(request):
    if request.method != 'POST':
        form = ChapterForm()
    else:
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save()
            return HttpResponseRedirect(reverse('works:get_story', args=[chapter.of_story.id]))

    context = {
        'form': form,
    }
    return render(request, 'works/new_chapter.html', context)


@login_required
def new_character(request):
    if request.method != 'POST':
        form = CharacterForm()
    else:
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            character = form.save()
            return HttpResponseRedirect(reverse('works:get_story', args=[character.of_story.id]))

    context = {
        'form': form,
    }
    return render(request, 'works/new_character.html', context)
