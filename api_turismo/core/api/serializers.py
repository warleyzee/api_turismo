from rest_framework import serializers
from core.models import PontosTuristicos
from atracaoes.api.serializers import AtracoesSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacaoes.api.serializers import AvaliacaoSerializer
from endereco.api.serializers import EnderecoSerializer


class PontosTuristicosSerializer(serializers.ModelSerializer):
    Atracaoes = AtracoesSerializer(many=True)
    Comentario = ComentarioSerializer(many=True)
    avaliacaoes = AvaliacaoSerializer(many=True)
    endereco = EnderecoSerializer()

    class Meta:
        model = PontosTuristicos
        fields = ['id', 'nome', 'descricao', 'fotos','Atracaoes', 'Comentario', 'avaliacaoes', 'endereco']