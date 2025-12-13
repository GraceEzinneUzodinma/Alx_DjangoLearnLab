from django.db import models
from accounts.models import CustomUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Notification(models.Model):
    recipient = models.ForeignKey (CustomUser)
    actor = models.ForeignKey(CustomUser)
    verb = models.CharField(max_length= 300)
    target_content_type = models.ForeignKey(ContentType, on_delete= models.CASCADE)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey ('target_content_type', 'target_object_id') 
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
