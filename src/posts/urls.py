from django.conf.urls import url
from django.contrib import admin
from .views import PostList

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
]
