from django.urls import path
from .views import *


urlpatterns = [
    path('create-product/', CreateProduct.as_view(), name='creat-product'),
    path('list-products/', ListProducts.as_view(), name='home'),
    path('edit-product/<int:pk>/', EditProduct.as_view(), name='edit-product'),
    path('delete-product/<int:pk>/', DeleteProduct.as_view(), name='delete-product')
]
