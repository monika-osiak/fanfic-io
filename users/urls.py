from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),

    path('<slug:username>', views.profile, name='profile'),
    path('<slug:username>/works', views.works, name='works'),
    path('<slug:username>/drafts', views.drafts, name='drafts'),
    path('<slug:username>/bookmarks', views.bookmarks, name='bookmarks'),

    path('<slug:username>/edit', views.edit, name='edit'),
    path('<slug:username>/change_username', views.change_username, name='change_username'),
    path('<slug:username>/change_password', views.change_password, name='change_password'),
    path('<slug:username>/change_email', views.change_email, name='change_email'),
]
