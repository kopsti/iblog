from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from iblog.utils import get_read_time, unique_slug_generator

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:category_detail", kwargs={"category": self.slug})

    class Meta:
        verbose_name_plural = "categories"

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

class Post(models.Model):
    author = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, editable=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/posts')
    content = models.TextField()
    draft = models.BooleanField(default=False)
    read_time =  models.IntegerField(default=0)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"post": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    # if instance.content:
    #     html_string = instance.get_markdown()
    #     read_time = get_read_time(html_string)
    #     instance.read_time = read_time_var
pre_save.connect(pre_save_receiver, sender=Post)
pre_save.connect(pre_save_receiver, sender=Category)
