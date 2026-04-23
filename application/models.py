from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    OPTION_CHOICES = [
        ('ML', 'MASALA LEMON'),
        ('GR', 'GINGER'),
        ('CL', 'CHILLI'),
        ('KL', 'KIWI LEMON'),
        ('AL', 'APPLE LEMON'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')    
    created_at = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=OPTION_CHOICES)      
    description2 = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """One to many relationship with product review"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review by {self.user.username} for {self.product.name}'

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    products_variety = models.ManyToManyField(Product, related_name='stores')
    
    def __str__(self):
        return self.name

class StoreOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateField(default=timezone.now)
    valid_until = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.store.name}'
    
class product_certificate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='certificates')
    certificate_name = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=100)
    issue_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.certificate_name} for {self.product.name}'
    
class product_image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'Image for {self.product.name}'
    
class product_video(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='product_videos/')

    def __str__(self):
        return f'Video for {self.product.name}'
    
class product_document(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='product_documents/')

    def __str__(self):
        return f'Document for {self.product.name}'
    
class product_faq(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f'FAQ for {self.product.name} - {self.question}'
    
class product_specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    specification_name = models.CharField(max_length=100)
    specification_value = models.CharField(max_length=255)

    def __str__(self):
        return f'Specification for {self.product.name} - {self.specification_name}'
    
class product_pricing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pricing')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'Pricing for {self.product.name} - {self.price}'
    
class product_inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Inventory for {self.product.name} - {self.quantity}'
    