from django.db import models


# Create your models here.
class Profissional(models.Model):
    nome = models.CharField(max_length=150)
    crm = models.IntegerField()

    def __str__(self):
        return self.nome
