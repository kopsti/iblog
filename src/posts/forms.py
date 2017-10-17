from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = ['title', 'category', 'image', 'content', 'draft', 'publish']
