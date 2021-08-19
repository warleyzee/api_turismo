from rest_framework import viewsets
from atracaoes.models import Atracaoes
from .serializers import AtracoesSerializer

class AtracoesViewSet(viewsets.ModelViewSet):
    queryset = Atracaoes.objects.all()
    serializer_class = AtracoesSerializer
    filter_fields = ('nome', 'descricao')