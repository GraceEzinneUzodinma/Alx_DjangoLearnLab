from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length= 200)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


# Create your models here.
