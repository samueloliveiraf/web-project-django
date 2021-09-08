from django.urls import path
from .views import *


urlpatterns = [
    path('cadastrar-empresa/', CreateCompany.as_view(), name='creat-company'),
    path('editar-empresa/<int:pk>/', EditCompany.as_view(), name='edit-company'),
    path('listar-empresa/', list_company, name='list-company'),
]
