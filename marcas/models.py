from django.db import models

class Marca(models.Model):
    nome = models.TextField(blank=False, null=False, max_length=50)

    def __str__(self):
        return self.nome