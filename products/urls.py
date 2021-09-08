from .pdfview import GeneratePDF
from django.urls import path
from .views import *


urlpatterns = [
    path('cadastrar-produto/', CreateProduct.as_view(), name='creat-product'),
    path('lista-produtos/', ListProducts.as_view(), name='home'),
    path('editar-produto/<int:pk>/', EditProduct.as_view(), name='edit-product'),
    path('deletar-produto/<int:id_product>/', delete_product, name='delete-product'),
    path('buscar/', search_products, name='search_products'),
    path('listar-vendas/', list_sales, name='list_sales'),
    path('venda/<int:id_product>/', sale_product, name='sale_product'),
    path('pdf/<int:id_sale>/', GeneratePDF.as_view(), name="pdf"),
]
