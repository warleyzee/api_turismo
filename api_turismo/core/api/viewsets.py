from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from core.models import PontosTuristicos
from .serializers import PontosTuristicosSerializer


class PontosTuristicosViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = PontosTuristicos.objects.all()
    serializer_class = PontosTuristicosSerializer
    filter_backends = [SearchFilter,]
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    search_fields = ['nome', 'descricao']

    def get_queryset(self):
        return PontosTuristicos.objects.filter(aprovado = True)

    def list(self, request, *args, **kwargs):
        return super(PontosTuristicosViewSet, self).list( request, *args, **kwargs)
    def create(self, request, *args, **kwargs):
        return super(PontosTuristicosViewSet, self).create( request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        return super(PontosTuristicosViewSet, self).destroy( request, *args, **kwargs)
    def retriever(self, request, *args, **kwargs):
        return super(PontosTuristicosViewSet, self).retriever( request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super(PontosTuristicosViewSet, self).update( request, *args, **kwargs)
    def partial_pudate(self, request, *args, **kwargs):
        return super(PontosTuristicosViewSet, self).partial_pudate( request, *args, **kwargs) 

    # @action(methods=['get'], detail=False)   
    # def teste(self, request):
    #     pass