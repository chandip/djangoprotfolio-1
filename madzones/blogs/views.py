from django.shortcuts import render
from . models import Blog
# Create your views here.
def blog_single_view(request, slug): # *args, **kwargs
    # print(args, kwargs)
    blog = Blog.objects.get(slug = slug)
    context = {
        'blog': blog,
        }
    # return HttpResponse(course)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "blogs/single.html", context)

def blog_view(request): # *args, **kwargs
    # print(args, kwargs)
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        }
    # return HttpResponse(course)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "blogs/index.html", context)
