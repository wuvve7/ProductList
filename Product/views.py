from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Company
from django.http import HttpResponse
from .forms import ProductForm
from django.contrib import messages

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})

def view_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'view_product.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إضافة المنتج بنجاح!")
            return redirect('list_products') 
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})
