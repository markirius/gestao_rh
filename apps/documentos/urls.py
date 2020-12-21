from django.urls import path
from apps.documentos.views import (
    DocumentoCreate,
    DocumentoList,
    DocumentoEdit,
    DocumentoDelete
)


urlpatterns = [
    path('', DocumentoList.as_view(), name="list_documento"),
    path('novo/<int:pk>', DocumentoCreate.as_view(), name="create_documento"),
    path(
        'editar/<int:pk>',
        DocumentoEdit.as_view(),
        name="update_documento"
    ),
    path(
        'deletar/<int:pk>',
        DocumentoDelete.as_view(),
        name="delete_documento"
    ),
]
