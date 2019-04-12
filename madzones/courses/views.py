from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from django.views import View
from madzones.pages.models import Page
# Create your views here.
def course_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    courses = Course.objects.all()
    pages = Page.objects.all()
    context = {
        'courses': courses,
        'blogs': pages,
    }
    # return HttpResponse(course)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "courses/index.html", context)


def course_single_view(request, slug): # *args, **kwargs
    # print(args, kwargs)
    course = Course.objects.get(slug = slug)
    childCourses = Course.objects.filter(parent = course)
    context = {
        'course': course,
        'childCourses': childCourses
    }
    # return HttpResponse(course)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "courses/single.html", context)


def course_child_single_view(request, slug, childSlug): # *args, **kwargs
    # print(args, kwargs)
    course = Course.objects.get(slug = childSlug)
    childCourses = Course.objects.filter(parent = course)
    context = {
        'course': course,
        'childCourses': childCourses
    }
    # return HttpResponse(course)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "courses/single.html", context)



