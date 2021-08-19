from rest_framework import serializers
from atracaoes.models import Atracaoes

class AtracoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atracaoes
        fields = ['id', 'nome', 'horario_func', 'data_evento', 'fotos']