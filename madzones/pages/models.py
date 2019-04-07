from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.template.defaultfilters import slugify


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank = True)
    content = models.TextField(blank=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(blank=True)

    date_posted = models.DateTimeField(default=timezone.now, blank = True)
    updated_date = models.DateTimeField(default=timezone.now, blank = True)
# Create your models here.

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title or str(self.slug)