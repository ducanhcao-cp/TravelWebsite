from django.shortcuts import render, redirect
from django.core.paginator import Paginator
#from django.http import HttpResponseRedirect
from .models import Special
from offers.models import Tours
from blog.models import Blog
from .forms import RegistrationForm 

def index(request):
    tourList = Tours.objects.all() 
    special = Special.objects.all()
    blogList = Blog.objects.all()
    paginator = Paginator(tourList, 9) 
    page_number = request.GET.get('page') 
    page_tour = paginator.get_page(page_number) 
    
    context = {'tourList':tourList,
                'special':special,
                'blogList':blogList,
                'page_tour':page_tour,
                 }
    return render(request, 'home/index.html', context) 

def register(request): 
    form = RegistrationForm(request.POST or None)  
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('/')
    return render(request, 'home/index.html', {'form':form})