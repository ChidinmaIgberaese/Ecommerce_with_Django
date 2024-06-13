#myapp/urls.py

from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list')
    # Add more URL patterns as needed
]