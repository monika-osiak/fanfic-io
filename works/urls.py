from django.urls import path

from . import views

app_name = 'works'
urlpatterns = [
    # .../works/
    path('', views.index, name='index'),
    # .../works/5/
    path('<int:story_id>/', views.get_story, name='get_story'),
    # .../works/5/chapters/
    path('<int:story_id>/chapters/', views.get_chapters, name='get_chapters'),
    # .../works/5/chapters/1
    path('<int:story_id>/chapters/<int:chapter_id>/', views.get_chapter, name='get_chapter'),
    # .../works/5/characters
    path('<int:story_id>/characters/', views.get_characters, name='get_characters'),
]
