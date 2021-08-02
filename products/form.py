
from django import forms
from .models import Product


class CustumerForm(forms.ModelForm):
    title = forms.CharField(label='Nome Produto')
    price = forms.IntegerField(label='Preço R$')
    quantity = forms.IntegerField(label='Quantidade')
    details = forms.CharField(label='Detalhamento')
    image = forms.ImageField()

    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'quantity',
            'details',
            'image',
        )