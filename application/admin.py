from django.contrib import admin
from .models import (
    ProductReview, Product, Store, StoreOwner, 
    product_certificate, product_image, product_video, 
    product_document, product_faq, product_specification, 
    product_pricing, product_inventory
)

# Register your models here.

class ProductReviewAdmin(admin.TabularInline):
    model = ProductReview
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type', 'created_at')
    search_fields = ('name', 'description')
    inlines = [ProductReviewAdmin]

admin.site.register(Product, ProductAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    list_filter = ('location',)

admin.site.register(Store, StoreAdmin)


class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'store', 'certificate_number', 'issued_date')
    search_fields = ('user__username', 'store__name')

admin.site.register(StoreOwner, StoreOwnerAdmin)


class ProductCertificateAdmin(admin.ModelAdmin):
    list_display = ('product', 'certificate_name', 'issued_by', 'issue_date')
    search_fields = ('product__name', 'certificate_name', 'issued_by')

admin.site.register(product_certificate, ProductCertificateAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ('product__name',)

admin.site.register(product_image, ProductImageAdmin)


class ProductVideoAdmin(admin.ModelAdmin):
    list_display = ('product', 'video')
    search_fields = ('product__name',)

admin.site.register(product_video, ProductVideoAdmin)


class ProductDocumentAdmin(admin.ModelAdmin):
    list_display = ('product', 'document')
    search_fields = ('product__name',)

admin.site.register(product_document, ProductDocumentAdmin)


class ProductFAQAdmin(admin.ModelAdmin):
    list_display = ('product', 'question', 'answer')
    search_fields = ('product__name', 'question')

admin.site.register(product_faq, ProductFAQAdmin)


class ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = ('product', 'specification_name', 'specification_value')
    search_fields = ('product__name', 'specification_name')

admin.site.register(product_specification, ProductSpecificationAdmin)


class ProductPricingAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'discount_price')
    search_fields = ('product__name',)

admin.site.register(product_pricing, ProductPricingAdmin)


class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'last_updated')
    search_fields = ('product__name',)

admin.site.register(product_inventory, ProductInventoryAdmin)
