from posts.models import Category
from django.template import Library

register = Library()

@register.simple_tag
def get_categories():
    categories = Category.objects.all()
    return categories
