from django.db import models
from django.contrib.auth.models import User
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

class UserProfile(models.Model):
    Choices= [
        ('admin', 'Admin'),
        ('librarian','Librarian'),
        ('member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    role  = models.CharField(max_length= 20, choices = Choices, default= 'viewer')

# Create your models here.
