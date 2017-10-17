from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .models import Post
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
