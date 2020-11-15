from django.urls import path
from apps.funcionarios.views import FuncionarioCreate


urlpatterns = [
    path('novo', FuncionarioCreate.as_view(), name="create_funcionario"),
]
