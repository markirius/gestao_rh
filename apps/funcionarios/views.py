from django.urls import reverse_lazy
from apps.funcionarios.models import Funcionario
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = "__all__"


class FuncionarioList(ListView):
    model = Funcionario

    # listar apenas funcionários da empresa do usuário logado
    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa)
        return queryset


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ["nome", "departamentos"]


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy("list_funcionario")
