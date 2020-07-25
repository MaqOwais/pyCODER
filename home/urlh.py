from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('',views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/',views.about,name='about'),
    path('search/',views.search,name='search'),
    path('signup/',views.handleSignup,name='handleSignup'),
    path('login/',views.handleLogin,name='handleLogin'),
    path('logout/',views.handleLogout,name='handleLogout'),
    path('archive/',views.archive,name='archive'),
    path('topic_page/<str:rewrite_topicsub>/',views.topic_page,name='topic_page'),
    path('books/',views.books,name='books'),
    path('archive/archive_page/<int:year>/<str:month>',views.archive_page,name='archive_page'),

]
