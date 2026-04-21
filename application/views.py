from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
# Create your views here.
def all_django(request):
    products = Product.objects.all()
    return render(request, 'frontend/all_django.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'frontend/product_detail.html', {'product': product})