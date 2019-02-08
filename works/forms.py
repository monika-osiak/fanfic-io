from django import forms

from .models import Story, Chapter, Character, Comment


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
        fields = ['title', 'content']
        labels = {
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': ''
        }