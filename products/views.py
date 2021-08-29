from products.form import CustumerForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from .models import *

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

    # def get_queryset(self):
    #     title = self.request.GET.get('title')
    #     if title:
    #         object_list = self.model.objects.filter(
    #             Q(title__icontains=title)
    #         )
    #     else:
    #         object_list = self.model.objects.all()
    #     return object_list


class EditProduct(UpdateView):
    model = Product
    form_class = CustumerForm


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('home')


def sale(request):
    product = Product.objects.get()
    sale = Sale.objects.get()
    if product.quantity > 0:
        product.quantity = sale.quantity - product.quantity
        product.quantity.save()
    return product
