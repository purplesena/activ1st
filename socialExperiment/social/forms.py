from attr import attrs
from django import forms
from .models import Post, Comment, Event


class EventForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5})
    )
    date = forms.DateField()
    location = forms.CharField(max_length=50)
    link = forms.URLField()

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'link']

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'share something with the world...'})
    )

    class Meta:
        model = Post
        fields = ['body']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'reply...'})
    )

    class Meta:
        model = Comment
        fields = ['comment']