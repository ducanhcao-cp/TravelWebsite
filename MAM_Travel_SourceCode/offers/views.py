from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def offers(request):
    tourList = Tours.objects.all() 
    context = {'tourList':tourList}
    return render(request, 'offers/offers.html',context)

def offersDetail(request, id):
    tourDetail = get_object_or_404(Tours, id=id)
    photos = tourImages.objects.filter(tours=tourDetail)
    context = {'tourDetail':tourDetail, 'photos':photos} 
    return render(request, 'offers/single_listing.html', context) 


def getDeal(request):
    form = DealForm() 
    if request.method == 'POST':
        form = DealForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('/')
    else:
        return render(request, 'offers/offers.html', {'form':form})

