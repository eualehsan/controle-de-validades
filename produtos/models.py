from django.db import models
from categorias.models import Categoria
from marcas.models import Marca

class Produto(models.Model):
    codigo_barras =  models.PositiveBigIntegerField(unique=False)
    descricao = models.TextField(blank=False, null=False, max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING) 