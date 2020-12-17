from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView
)

from apps.funcionarios.models import Funcionario


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ["nome", "departamentos"]
    success_url = reverse_lazy("list_funcionario")

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = (
            funcionario.nome.split(" ")[0]+"."+funcionario.nome.split(" ")[1]
        ).lower()
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(
            username=username
        )
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


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
