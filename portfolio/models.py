# models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey('Portfolio', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images', blank=True)

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)  # Allow null and blank for now
    short_detail = models.CharField(max_length=500, blank=True)
    details = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate slug from the title
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("portfolio_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Portfolio"
        ordering = ["title"]

    def __str__(self):
        return self.title
