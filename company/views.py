from company.form import CustumerForm
from company.models import Company
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    UpdateView,
    CreateView
)


class CreateCompany(CreateView):
    model = Company
    form_class = CustumerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateCompany, self).form_valid(form)


class EditCompany(UpdateView):
    model = Company
    form_class = CustumerForm


@login_required(login_url='/accounts/login/')
def list_company(request):
    template_name = 'company/page_company.html'
    companys = Company.objects.filter(
        user=request.user
    )

    context = {
        'companys': companys,
    }

    return render(request, template_name, context)

