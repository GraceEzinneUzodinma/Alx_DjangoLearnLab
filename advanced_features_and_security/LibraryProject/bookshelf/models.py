from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo):
        user = self.model(
            date_of_birth= date_of_birth,
            profile_photo= profile_photo
        )
        user.save(using = self._db)
        return user

    def create_superuser(self, date_of_birth, profile_photo):
        user = self.create_user(
            date_of_birth= date_of_birth,
            profile_photo= profile_photo
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
class CustomUser(AbstractUser):
    date_of_birth = models.DateField
    profile_photo = models.ImageField
    is_staff = models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    objects = CustomUserManager()
class Meta:
    permissions  =[
        ('can_view', 'can view'),
        ('can_create', 'can create'),
        ('can_edit', 'can edit'),
        ('can_delete', 'can delete' ),
    ]
# Create your models here.
