from django.urls import path
from apps.funcionarios.views import FuncionariosCreate, FuncionariosList


urlpatterns = [
    path('', FuncionariosList.as_view(), name="list_funcionario"),
    path('novo', FuncionariosCreate.as_view(), name="create_funcionario"),
]
