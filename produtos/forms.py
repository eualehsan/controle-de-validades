from django import forms
from .models import Produto

class ProdutoForm(forms.Form):
    class Meta:
        model = Produto
        fields = ['codigo_barras', 'descricao', 'tipo', 'marca']