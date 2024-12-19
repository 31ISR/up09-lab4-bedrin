from django.contrib import admin 
from django.urls import path, include
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.communities_list, name='list'),
    path('create/', views.create_community, name='community_create'),
    path('new-community', views.create_community, name='new-community')
]
