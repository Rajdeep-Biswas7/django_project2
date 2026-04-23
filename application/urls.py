from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.all_django, name='all_django'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/images/', views.product_images, name='product_images'),
    path('product/<int:product_id>/videos/', views.product_videos, name='product_videos'),
    path('product/<int:product_id>/documents/', views.product_documents, name='product_documents'),
    path('product/<int:product_id>/faqs/', views.product_faqs, name='product_faqs'),
    path('product/<int:product_id>/specifications/', views.product_specifications, name='product_specifications'),
    path('product/<int:product_id>/pricing/', views.product_pricing, name='product_pricing'),
    path('product/<int:product_id>/inventory/', views.product_inventory, name='product_inventory'),

]
