from django.contrib import admin
from django.urls import path , include
from . import views
# from .feeds import LatestPostsFeed
### lets make it bloggg


urlpatterns = [
    #api to post a comment
    path('postComment',views.postComment, name = 'postComment'),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>/', views.blogPost, name='blogPost'),
]
