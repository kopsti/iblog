from django.conf.urls import url
from django.contrib import admin
from .views import PostCreate, PostDetail, PostList

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^create/$', PostCreate.as_view(), name='post_create'),
    url(r'^(?P<post>[\w-]+)/$', PostDetail.as_view(), name='post_detail'),
]
