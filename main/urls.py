from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('home/', views.home, name='home'),
    path('add-post/', views.add_post, name='add-post'),
    path('add-friend/', views.add_friend, name='add-friend'),
    path('add-comment/<int:post_id>/', views.add_comment, name='add-comment'),
    path('show-friends', views.show_friends, name='show-friends'),
]
