from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=120)
    body = forms.CharField(max_length=240)

    class Meta:
        model = Post
        fields = ('title', 'body', )

class CommentForm(forms.ModelForm):
    body = forms.CharField(max_length=240, 
        widget=forms.TextInput(attrs={
            'id': 'commentBody',
        }))

    class Meta:
        model = Comment
        fields = ('body', )