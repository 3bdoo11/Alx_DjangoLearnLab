from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # <-- import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # add 'tags'
        widgets = {
            'tags': TagWidget(),  # enable tag input widget
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'})
        }
