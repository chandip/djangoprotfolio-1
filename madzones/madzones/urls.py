"""madzones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from frontend.views import frontend_view, aboutme_view
from courses.views import course_single_view
from courses.views import course_child_single_view
from courses.views import course_view
from quizes.views import quiz_view
from blogs.views import blog_single_view
from blogs.views import blog_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontend_view, name='home'),
    path('courses/<slug>/<childSlug>', course_child_single_view),
    path('courses/<slug>', course_single_view),
    path('blogs/<slug>', blog_single_view),
    path('about/', aboutme_view),
    path('blogs/', blog_view),
    path('courses/', course_view),
    path('quizes/', quiz_view),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)