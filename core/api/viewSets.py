from rest_framework.viewsets import ModelViewSet
from core.models import TouristSpot
from .serializers import TouristSpotSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class TouristSpotViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = TouristSpotSerializer

    # ACTIONS

    # Executado para fazer a filtragem de resultados
    def get_queryset(self):
        return TouristSpot.objects.filter(okay=True)

    # Executado na exibicao da lista de resultados
    # def list(self, request, *args, **kwargs):
    #     return Response({'teste': 123})

    # Executando quando um recurso vai ser criado
    # def create(self, request, *args, **kwargs):
    #     return Response({'Hello': request.data['name']})

    # Executado quando um recurso vai ser deletado
    # def destroy(self, request, *args, **kwargs):
    #     pass

    # Executado, assim como o LIST, quando o usuario pede para ver os
    # dados dos recursos, mas esse metodo e executado quando
    # quando eu quero obter um recurso em especifico e nao
    # a lista de todos os recursos presentes no banco
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # Executado quando um recurso vai ser atualizado por inteiro (PUT)
    # def update(self, request, *args, **kwargs):
    #     pass

    # Executado quando apenas parte de um recurso vai ser atualizado (PATCH)
    # def partial_update(self, request, *args, **kwargs):
    #     pass


    # CUSTOM ACTIONS

    # Custom Action que trabalhar com um recurso especifico
    # @action(methods=['get'], detail=True)
    @action(methods=['post', 'get'], detail=True)
    def denounce(self, request, pk=None):
        return Response({'denounce': pk})
        pass

    
    # Custom Action que trabalha com um conjunto de recursos
    @action(methods=['get'], detail=False)
    def testAllList(self, request):
        return Response({'testAllList': 'sucess'})
