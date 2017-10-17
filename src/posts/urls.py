from django.conf.urls import url
from django.contrib import admin
from .views import PostAuthorList, PostCategoryDetail, PostCreate, PostDelete, PostDetail, PostList, PostUpdate

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^create/$', PostCreate.as_view(), name='post_create'),
    url(r'^post/(?P<post>[\w-]+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^author/(?P<user>[\w-]+)/$', PostAuthorList.as_view(), name='post_author'),
    url(r'^category/(?P<category>[\w-]+)/$', PostCategoryDetail.as_view(), name='category_detail'),
    url(r'^update/(?P<post>[\w-]+)/$', PostUpdate.as_view(), name='post_update'),
    url(r'^delete/(?P<post>[\w-]+)/$', PostDelete.as_view(), name='post_delete'),
]
