from django.contrib import admin
from django.urls import path, include
from . import views



from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('about/', views.about),
    path('posts/', include('posts.urls')),
    path('communities/', include('communities.urls')),
    path('', views.index),
    path('', include('communities.urls')),
]

