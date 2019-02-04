from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    # ...
    path('', views.index, name='index'),
    # .../admin
    path('<slug:username>', views.profile, name='profile'),
]