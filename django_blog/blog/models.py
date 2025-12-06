from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
class Post(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey( User, on_delete= models.CASCADE, related_name= 'post')
    tags = TaggableManager(blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name= 'comment')
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Tag(models.Model):
    name = models.CharField(max_length= 200)
    posts = models.ManyToManyField(Post, blank= True)

# Create your models here.
