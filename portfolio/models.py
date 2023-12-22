# posts/models.py
from django.db import models
from ckeditor.fields import RichTextField 
from django.urls import reverse


class PortFolio(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    
    def __str__(self): # new
        return self.title
    
    def get_absolute_url(self):
        return reverse("portfolio_detail", args=[str(self.id)])