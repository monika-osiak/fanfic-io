from django.contrib import admin

from .models import Story, Chapter, Character, Comment

admin.site.register(Story)
admin.site.register(Chapter)
admin.site.register(Character)
admin.site.register(Comment)
