from django import forms
from .models import * 

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = '__all__'