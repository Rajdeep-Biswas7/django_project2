from django.http import HttpResponse 
from django.shortcuts import render 
from application.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'website/index.html', {'products': products})

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def services(request):
    return render(request, 'website/services.html')
def products(request):
    return render(request, 'website/products.html')