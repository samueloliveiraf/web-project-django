from django.urls import path
from .views import *


urlpatterns = [
    path('cadastrar-produto/', CreateProduct.as_view(), name='creat-product'),
    path('lista-produtos/', ListProducts.as_view(), name='home'),
    path('editar-produto/<int:pk>/', EditProduct.as_view(), name='edit-product'),
    path('deletar-produto/<int:pk>/', DeleteProduct.as_view(), name='delete-product'),
    path('buscar/', search_products, name='search_products')
]
