from django.shortcuts import render 
from .models import Blog 
# Create your views here.

def blog(request): 
    blogList = Blog.objects.all() 
    context = {'blogList':blogList} 
    return render(request, 'blog/blog.html', context) 

def blogDetail(request, id):
    blogDetail = Blog.objects.get(id = id) 
    context = {'blogDetail':blogDetail} 
    return render(request, 'blog/blogDetail.html', context) 
