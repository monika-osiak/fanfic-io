from django.urls import path

from . import views

app_name = 'works'
urlpatterns = [
    # .../works/
    path('', views.IndexView.as_view(), name='index'),
    # .../works/5/
    path('<int:story_id>/', views.get_story, name='get_story'),
    # .../works/5/chapters/1
    path('<int:story_id>/chapters/<int:chapter_number>/', views.get_chapter, name='get_chapter'),
    # .../works/5/characters/1
    path('<int:story_id>/characters/<int:pk>/', views.CharacterView.as_view(), name='get_character'),
    # .../works/new_story
    path('new_story/', views.new_story, name='new_story'),
    # .../works/5/new_chapter
    path('<int:story_id>/new_chapter/', views.new_chapter, name='new_chapter'),
    # .../works/5/new_character
    path('<int:story_id>/new_character/', views.new_character, name='new_character')
]