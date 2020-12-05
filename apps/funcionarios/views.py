from apps.funcionarios.models import Funcionario
from django.views.generic import CreateView, ListView


class FuncionariosCreate(CreateView):
    model = Funcionario
    fields = "__all__"


class FuncionariosList(ListView):
    model = Funcionario

    # listar apenas funcionários da empresa do usuário logado
    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa)
        return queryset
