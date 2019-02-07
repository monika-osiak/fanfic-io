from django import forms

from .models import Story, Chapter, Character

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title']
        labels = {
            'title': 'Title:'
        }


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['number', 'title', 'content']
        labels = {
            'number': 'Chapter number:',
            'title': 'Title:',
            'content': ''
        }


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'image']
        labels = {
            'name': 'Full name:',
            'image': 'Picture:'
        }
