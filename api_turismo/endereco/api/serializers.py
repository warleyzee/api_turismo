from rest_framework import serializers
from endereco.models import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'rua', 'numero', 'bairro', 'cidade', 'ponto_referencia', 'longitude', 'latitude']
