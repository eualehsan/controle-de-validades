from django.db import models

class Categoria(models.Model):
    nome = models.TextField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome