from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView
)

from apps.documentos.models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ["descricao", "arquivo"]
    # success_url = reverse_lazy("list_documento")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs["pk"]

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DocumentoList(ListView):
    model = Documento

    # listar apenas funcionários da empresa do usuário logado
    # def get_queryset(self):
    #     empresa = self.request.user.documento.empresa
    #     queryset = Documento.objects.filter(empresa=empresa)
    #     return queryset


class DocumentoEdit(UpdateView):
    model = Documento
    fields = ["nome", "departamentos"]
    success_url = reverse_lazy("list_documento")


class DocumentoDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy("list_documento")
