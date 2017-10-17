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

admin.site.register(Post, PostAdmin)
