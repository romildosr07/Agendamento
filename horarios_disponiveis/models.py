from django.db import models


# Create your models here.
class Horario(models.Model):
    dia_da_semana = models.CharField(max_length=7)
    hora = models.TimeField()

    def __str__(self):
        return self.dia_da_semana
