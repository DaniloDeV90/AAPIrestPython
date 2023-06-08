from django.db import models

# Create your models here.
class Processo (models.Model):
     multa = models.DecimalField (decimal_places=100,max_digits=100 )
     autor =  models.CharField (max_length= 100)
     réu = models.CharField (max_length=100)
     juiz = models.CharField (max_length=100)
     recurso_especial = models.CharField (max_length=100)