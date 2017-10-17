from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Category, Post, User
from .forms import PostForm
# Create your views here.

class PostCreate(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

class PostList(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.active()
        if (self.request.user.is_staff or self.request.user.is_superuser):
            queryset = Post.objects.all()
        return queryset

class PostDetail(DetailView):
    model = Post
    slug_url_kwarg = 'post'

    def get_queryset(self):
        queryset = Post.objects.active()
        if (self.request.user.is_staff or self.request.user.is_superuser):
            queryset = Post.objects.all()
        return queryset

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    slug_url_kwarg = 'post'

class PostDelete(DeleteView):
    model = Post
    slug_url_kwarg = 'post'

    def get_success_url(self):
        author = self.object.author.username
        return reverse_lazy('posts:post_author', kwargs={'user': author})

class PostAuthorList(ListView):
    model = Post
    template_name_suffix = '_author'
    context_object_name = 'posts'

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs['user'])
        queryset = Post.objects.active()
        if (self.request.user.is_staff or self.request.user.is_superuser):
            queryset = Post.objects.all()
        queryset = queryset.filter(author=author)
        return queryset

class PostCategoryDetail(ListView):
    model = Post
    context_object_name = 'tools'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['category'])
        queryset = Post.objects.active()
        if (self.request.user.is_staff or self.request.user.is_superuser):
            queryset = Post.objects.all()
        queryset = queryset.filter(category=category)
        return queryset
