from rest_framework import viewsets
from avaliacaoes.models import Avaliacaoes
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Avaliacaoes.objects.all()
    serializer_class = AvaliacaoSerializer