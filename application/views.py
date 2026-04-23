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

def product_images(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    images = product.images.all()
    return render(request, 'frontend/product_images.html', {'product': product, 'images': images})

def product_videos(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    videos = product.videos.all()
    return render(request, 'frontend/product_videos.html', {'product': product, 'videos': videos})

def product_documents(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    documents = product.documents.all()
    return render(request, 'frontend/product_documents.html', {'product': product, 'documents': documents})

def product_faqs(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    faqs = product.faqs.all()
    return render(request, 'frontend/product_faqs.html', {'product': product, 'faqs': faqs})

def product_specifications(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    specifications = product.specifications.all()
    return render(request, 'frontend/product_specifications.html', {'product': product, 'specifications': specifications})

def product_pricing(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    pricing = product.pricing.all()
    return render(request, 'frontend/product_pricing.html', {'product': product, 'pricing': pricing})

def product_inventory(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    inventory = product.inventory.all()
    return render(request, 'frontend/product_inventory.html', {'product': product, 'inventory': inventory})

