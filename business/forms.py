from django import forms
from .models import Business

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name','description','employee_size','address','phone_number','owner_name','owner_phone_number','website')
