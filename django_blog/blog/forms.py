from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # <-- import TagWidget from django-taggit

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # <-- add tags field
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Add tags separated by commas'}),  # nice input for tags
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'})
        }
