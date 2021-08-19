from django.db import models

# Create your models here.

class Atracaoes(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    data_evento = models.TextField()
    idade_minima = models.IntegerField()
    fotos = models.ImageField(upload_to='atracoes', null=True, blank=True)

    def __str__(self):
        return self.nome
