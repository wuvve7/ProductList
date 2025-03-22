from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('products/', views.list_products, name='list_products'),
    path('products/<int:product_id>/', views.view_product, name='view_product'),
    path('products/add/', views.add_product, name='add_product'),  
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)