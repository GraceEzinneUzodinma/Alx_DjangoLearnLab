from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length= 200)
    content = models.TextField(default= '')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    content = models.TextField(default= '')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
