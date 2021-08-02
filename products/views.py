from products.form import CustumerForm
from django.urls import reverse_lazy
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


class EditProduct(UpdateView):
    model = Product
    form_class = CustumerForm


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('home')
