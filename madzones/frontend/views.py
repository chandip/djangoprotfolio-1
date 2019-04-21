from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course
from pages.models import Page
from blogs.models import Blog


# Create your views here.
def frontend_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    courses = Course.objects.filter(parent = None)
    #allCourses = Course.objects.all()
    coursesAll = []
    for course in courses:
        childs = Course.objects.filter(parent = course)
        course.childs = childs
        coursesAll.append(course)

    pages = Page.objects.all()
    blogs = Blog.objects.all()
    context = {
        'courses': courses,
        'blogs': pages,
        'coursesAll': coursesAll,
        'blogs': blogs,

    }
    # return HttpResponse(course)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", context)

def aboutme_view(request):
    return render(request, 'aboutme.html')
