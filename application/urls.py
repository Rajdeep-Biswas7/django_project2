from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
  path('all-django/', views.all_django, name='all_django'),

]
