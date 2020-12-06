from django.urls import path
from apps.funcionarios.views import (
    FuncionarioCreate,
    FuncionarioList,
    FuncionarioEdit,
    FuncionarioDelete
)


urlpatterns = [
    path('', FuncionarioList.as_view(), name="list_funcionario"),
    path('novo', FuncionarioCreate.as_view(), name="create_funcionario"),
    path(
        'editar/<int:pk>',
        FuncionarioEdit.as_view(),
        name="update_funcionario"
    ),
    path(
        'deletar/<int:pk>',
        FuncionarioDelete.as_view(),
        name="delete_funcionario"
    ),
]
