from hashlib import blake2b
from pickle import TRUE
from ssl import create_default_context
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from multiselectfield import MultiSelectField
from django.dispatch import receiver

TOPIC_CHOICES = (
    ('int_conflict','International Conflicts'),
    ('w_rights', 'Women\'s Rights'),
    ('unions', 'Unions / Strikes / etc.'),
    ('blm', 'BLM'),
    ('imgrtn', 'Immigration'),
    ('lgbt', 'LGBTQ+')
)

class Protest(models.Model):
    #what the user types
    body = models.TextField()
    title = models.CharField(max_length=200, default="This is a Protest !")
    created_on = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='static/images', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    keyword = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)


class Post(models.Model):
    #what the user types
    body = models.TextField()
    #cant change date current time 
    created_on = models.DateTimeField(default=timezone.now)
    #deletes all comments n shit and finds the user
    image1 = models.ImageField(upload_to='uploads/post_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/post_images', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    pronouns = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.jpg')
    is_verified = models.BooleanField(default=False)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    preferred = MultiSelectField(max_length=50, choices=TOPIC_CHOICES, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()