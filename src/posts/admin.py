from django.contrib import admin
from .models import Category, Post

# Register your models here.

####### CATEGORY #######
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

admin.site.register(Category, CategoryAdmin)

####### POST #######
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'publish', 'updated', 'draft']
    list_display_links = ['title']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'author__username', 'content']

admin.site.register(Post, PostAdmin)
