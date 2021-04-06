from django.shortcuts import render, redirect 
from .models import Contact 
from .forms import ContactForm 
from django.views import View 
# Create your views here.
class contact(View): 
    def get(self, request):
        context = {'ContactForm' : ContactForm}
        return render(request, 'contact/contact.html', context) 

    def post(self, request):
        form = ContactForm() 
        if request.method == 'POST':
            form = ContactForm(request.POST) 
            if form.is_valid:
                form.save() 
                return redirect('/')
        else:
            return render(request, 'contact/contact.html')
