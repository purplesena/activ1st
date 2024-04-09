from attr import attrs
from django import forms
from .models import Post, Comment, Protest

TOPIC_CHOICES = (
    ('int_conflict','International Conflicts'),
    ('w_rights', 'Women\'s Rights'),
    ('unions', 'Unions / Strikes / etc.'),
    ('blm', 'BLM'),
    ('imgrtn', 'Immigration'),
    ('lgbt', 'LGBTQ+')
)

class ProtestForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'explain your cause in as much detail as you want ! format: [quick summary][everything else]'})
    )
    date = forms.DateField()
    location = forms.CharField(max_length=100)
    keyword = forms.ChoiceField(choices=TOPIC_CHOICES)
    link = forms.URLField()
    image = forms.ImageField(required=False)

    class Meta:
        model = Protest
        fields = ['body', 'keyword', 'title', 'image', 'date', 'location', 'link']

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'share something with the world...'})
    )
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['body', 'image1', 'image2' ]

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'reply...'})
    )

    class Meta:
        model = Comment
        fields = ['comment']