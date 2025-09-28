from django.db import models
from categorias.models import Categoria
from marcas.models import Marca
from django.contrib.auth.models import User

class Produto(models.Model):
    imagem = models.TextField(default="//pic.pngsucai.com/00/21/38/c47a08b07905ecb0.webp")
    codigo_barras =  models.PositiveBigIntegerField(unique=False)
    descricao = models.TextField(blank=False, null=False, max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    criado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descricao