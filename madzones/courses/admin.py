from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from courses.models import Course

# Register your models here.

admin.site.register(Course, MPTTModelAdmin)
MPTT_ADMIN_LEVEL_INDENT = 1000
