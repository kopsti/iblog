from django.db import models
from django.db.models.signals import pre_save
from iblog.utils import unique_slug_generator
from django.conf import settings

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"
            
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, editable=False, unique=True)
    category = models.ForeignKey(Category)
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
        return reverse("posts:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=Post)
