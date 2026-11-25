from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class EBooks(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    objectives = models.CharField(max_length=2000, null=True, blank=True)
    image_url = models.CharField(max_length=5000, null=True, blank=True)
    story = models.CharField(max_length=500000, null=True, blank=True)
    posted_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    def __str__(self):
        return f"{self.title} written by {self.author}"
    
    

class Resources(models.Model):
    ebooks = models.ForeignKey(EBooks, on_delete=models.CASCADE, related_name='resource_books')
    resource_link = models.CharField(max_length=500)
    posted_on = models.DateTimeField(default=timezone.now)