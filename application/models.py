from django.db import models
from django.utils import timezone
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