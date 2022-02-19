from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    telefone =models.IntegerField()

    def __str__(self):
        return self.nome