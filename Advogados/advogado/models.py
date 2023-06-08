from django.db import models

# Create your models here.
class Advogado (models.Model): 
    OAB = models.IntegerField (max_length= 23)
    nome = models.CharField (max_length= 100)
    idade = models.CharField (max_length= 100)
    telefone = models.IntegerField (max_length = 100)
    Email = models.CharField (max_length= 100)