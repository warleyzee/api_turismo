from rest_framework import viewsets
from endereco.models import Endereco
from .serializers import EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer