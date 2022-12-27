from django.db import models

class Familiar(models.Model):
    name = models.CharField(max_length=100)
    edad = models.FloatField()
    casado = models.BooleanField()
