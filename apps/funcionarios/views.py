from apps.funcionarios.models import Funcionario
from django.views.generic.edit import CreateView


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = "__all__"
