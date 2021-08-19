from django.db import models
from atracaoes.models import Atracaoes
from comentarios.models import Comentario 
from avaliacaoes.models import Avaliacaoes
from endereco.models import Endereco


#Parametros dos pontos turisticos
class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=True)
    Atracaoes = models.ManyToManyField(Atracaoes)
    Comentario = models.ManyToManyField(Comentario)
    avaliacaoes = models.ManyToManyField(Avaliacaoes)
    endereco = models.ForeignKey (Endereco, on_delete=models.CASCADE, null=True, blank=True)
    fotos = models.ImageField(upload_to='pontos_turistico', null=True, blank=True)

    def __str__(self):
        return self.nome

