from products.form import *
from django.urls import reverse_lazy
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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
    paginate_by = 8
    ordering = ['-date']

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


@login_required(login_url='/accounts/login/')
def list_sales(request):
    template_name = 'products/list_sales.html'

    sales = Sale.objects.filter(
        user=request.user
    )

    product = Product.objects.filter(
        user=request.user
    )

    context = {
        'sales': sales,
        'product': product,
    }

    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def delete_product(request, id_product):
    product = Product.objects.get(
        id=id_product,
        user=request.user
    )

    product.delete()

    return redirect('home')

@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def sale_product(request, id_product):
    template_name = 'sale_product.html'
    product = Product.objects.get(id=id_product, user=request.user)

    quantity = request.POST.get("quantity")
    payment = request.POST.get("payment")

    if product.quantity > 0:
        sales = Sale(
            quantity=quantity,
            product=product, 
            payment=payment,
            user=request.user,
        )
        sales.save()
        
        product.quantity = product.quantity-int(quantity)
        product.save()

    context = {
        'sales': sales,
        'quantity': quantity,
        'product': product,
    }

    return render(request, template_name, context)
