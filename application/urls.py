from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.all_django, name='all_django'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    

]
