from django.urls import reverse_lazy
from apps.departamentos.models import Departamento
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)


class DepartamentoCreate(CreateView):
    pass


class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoEdit(UpdateView):
    pass


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy("list_departamento")
