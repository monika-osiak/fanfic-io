from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('<slug:username>/', views.profile, name='profile'),
    path('<slug:username>/update', views.update_profile, name='update_profile'),
]

# TODO:
# username/ -> dashboard
# username/profile/ -> profile
# username/works -> all work of user
# username/drafts -> unposted drafts
# username/bookmarks -> bookmarked stories
