# posts/models.py
from django.db import models
from ckeditor.fields import RichTextField 
from django.urls import reverse


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    detail = RichTextField()
    
    def __str__(self): # new
        return self.name
    
    def get_absolute_url(self):
        return reverse("service_detail", args=[str(self.id)])