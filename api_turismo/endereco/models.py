from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Endereco(models.Model):
    rua = models.CharField(max_length=150)
    numero = models.CharField(max_length=150)
    bairro = models.TextField(max_length=150)
    cidade = models.CharField(max_length=150)
    ponto_referencia = models.CharField(max_length=150)
    longitude = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)

    def __srt__ (self):
        return self.rua
