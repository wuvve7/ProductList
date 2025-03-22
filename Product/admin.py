from django.contrib import admin

# Register your models here.
from .models import Product, Company

admin.site.register(Product)
admin.site.register(Company)
