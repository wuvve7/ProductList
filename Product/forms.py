from django import forms
from .models import Product,Company

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['kind', 'company', 'expire_year']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address']