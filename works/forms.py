from django import forms

from .models import Story, Chapter, Character, Comment


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'description']
        labels = {
            'title': 'Title:',
            'description': 'Short description of the story:'
        }


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'content']
        labels = {
            'title': 'Title:',
            'content': ''
        }


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'image', 'description']
        labels = {
            'name': 'Full name:',
            'image': 'Picture:',
            'description': 'Short info about the character:'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': ''
        }