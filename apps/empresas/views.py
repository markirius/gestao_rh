from django.http import HttpResponse
from apps.empresas.models import Empresa
from django.views.generic.edit import CreateView, UpdateView


class EmpresaCreate(CreateView):
    model = Empresa
    fields = "__all__"

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse("Ok")


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = "__all__"
