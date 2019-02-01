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
        fields = ['of_story', 'number', 'title', 'content']
        labels = {
            'of_story': 'Story:',
            'number': 'Chapter number:',
            'title': 'Title:',
            'content': ''
        }


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'of_story', 'image']
        labels = {
            'name': 'Full name:',
            'of_story': 'Story:',
            'image': 'Picture:'
        }