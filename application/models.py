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
            
            #one to one relationship with store and user
            
class StoreOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateField(default=timezone.now)
    valid_until = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.store.name}'