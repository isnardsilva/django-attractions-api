from rest_framework.viewsets import ModelViewSet
from core.models import TouristSpot
from .serializers import TouristSpotSerializer
from rest_framework.response import Response

class TouristSpotViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = TouristSpotSerializer

    # Executado para fazer a filtragem de resultados
    def get_queryset(self):
        return TouristSpot.objects.filter(okay=True)

    # Executado na exibicao da lista de resultados
    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})

    # Executando quando um recurso vai ser criado
    def create(self, request, *args, **kwargs):
        return Response({'Hello': request.data['name']})

    # Executado quando um recurso vai ser deletado
    def destroy(self, request, *args, **kwargs):
        pass

    # Executado, assim como o LIST, quando o usuario pede para ver os
    # dados dos recursos, mas esse metodo e executado quando
    # quando eu quero obter um recurso em especifico e nao
    # a lista de todos os recursos presentes no banco
    def retrieve(self, request, *args, **kwargs):
        pass

    # Executado quando um recurso vai ser atualizado por inteiro
    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass