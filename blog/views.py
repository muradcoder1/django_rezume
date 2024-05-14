from django.shortcuts import render
def blog(request):
    return render(request, "blog.html")
def single_blog(request):
    return render(request, "single-blog.html")
# Create your views here.
