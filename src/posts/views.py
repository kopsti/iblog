from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Category, Post, User
from .forms import PostForm

# Create your views here.

class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    login_url = '/accounts/login/'
    success_message = 'Post created!'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

class PostList(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = Post.objects.active()
        if (self.request.user.is_staff or self.request.user.is_superuser):
            queryset = Post.objects.all()
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__username__icontains=query)
            ).distinct()
        return queryset

class PostDetail(DetailView):
    model = Post
    slug_url_kwarg = 'post'

    def get_queryset(self):
        queryset = Post.objects.active()
        if (self.request.user.is_staff or self.request.user.is_superuser):
            queryset = Post.objects.all()
        return queryset

class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    login_url = '/accounts/login/'
    slug_url_kwarg = 'post'
    success_message = 'Post updated!'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    login_url = '/accounts/login/'
    slug_url_kwarg = 'post'
    success_message = 'Post deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        author = self.object.author.username
        return reverse_lazy('posts:post_author', kwargs={'user': author})

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostAuthorList(ListView):
    model = Post
    template_name_suffix = '_author'
    context_object_name = 'posts'

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs['user'])
        query = self.request.GET.get("q")
        queryset = Post.objects.active()
        if (self.request.user.is_staff or self.request.user.is_superuser):
            queryset = Post.objects.all()
        queryset = queryset.filter(author=author)
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__username__icontains=query)
            ).distinct()
        return queryset

class PostCategoryDetail(ListView):
    model = Post
    context_object_name = 'tools'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['category'])
        query = self.request.GET.get("q")
        queryset = Post.objects.active()
        if (self.request.user.is_staff or self.request.user.is_superuser):
            queryset = Post.objects.all()
        queryset = queryset.filter(category=category)
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__username__icontains=query)
            ).distinct()
        return queryset
