from products.form import CustumerForm
from django import forms
from django.urls import reverse_lazy
from django.db.models import Q
from .models import *
from django.shortcuts import render

from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)


class CreateProduct(CreateView):
    model = Product
    form_class = CustumerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProduct, self).form_valid(form)


class ListProducts(ListView):
    model = Product
    paginate_by = 4

    def get_queryset(self):
        queryset = super(ListProducts, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class EditProduct(UpdateView):
    model = Product
    form_class = CustumerForm


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('home')


def search_products(request):
    template_name = 'search_product.html'
    title = request.GET.get('title')
    products = Product.objects.filter(
        title__icontains=title, user=request.user
    )

    context = {
        'products': products
    }

    return render(request, template_name, context)


def sale_product(request, id_product):
    template_name = 'sale_product.html'
    product = Product.objects.get(id=id_product)
    if product.quantity > 0:
        quantity = request.POST.get("quantity")
        quantity = 1

    sales = Sale(quantity=quantity, product=product)
    sales.save()
    product.quantity = product.quantity-int(quantity)
    product.save()

    context = {
        'sales': sales,
        'quantity': quantity, 
        'product': product,
    }

    return render(request, template_name, context)
