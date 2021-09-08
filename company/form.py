from company.models import Company
from django import forms


class CustumerForm(forms.ModelForm):
    name = forms.CharField(label='Nome da empresa')
    image = forms.ImageField()

    class Meta:
        model = Company
        fields = (
            'name',
            'image',
        )