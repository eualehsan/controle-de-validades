from django.db import models
from produtos.models import Produto
from datetime import date

class Validade(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="validades")
    estoque = models.PositiveIntegerField(blank=False, null=False)
    dt_validade = models.DateField(blank=False, null=False)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    @property
    def dias_p_vencer(self):
        hoje = date.today()
        return (self.dt_validade - hoje).days
    
    @property
    def dias_vencido(self):
        hoje = date.today()
        return (hoje - self.dt_validade).days

