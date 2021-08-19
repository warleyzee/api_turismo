from rest_framework import serializers
from avaliacaoes.models import Avaliacaoes


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacaoes
        fields = ['id','user', 'comentario', 'nota', 'data']