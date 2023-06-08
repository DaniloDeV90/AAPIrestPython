from django.db import models

# Create your models here.
class Cliente (models.Model):
    nome = models.CharField (max_length = 100)
    idade = models.CharField (max_length = 100)
    sexo = models.CharField (max_length = 50)
    cpf = models.CharField (max_length = 11)
    Email = models.CharField (max_length = 100)