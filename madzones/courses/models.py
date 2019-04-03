from django.db import models
from django.utils import timezone
from PIL import Image
from django.template.defaultfilters import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Course(MPTTModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    short_description = models.TextField(max_length=1000, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now, blank = True)
    updated_date = models.DateTimeField(default=timezone.now, blank = True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=False)
        except:
            ancestors = []
        else:
            ancestors = [i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i + 1]))
        return slugs

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = ('parent', 'slug',)
        verbose_name_plural = 'courses'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title or str(self.slug)
