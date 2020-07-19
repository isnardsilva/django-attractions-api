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
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        queryset = TouristSpot.objects.all()

        if id:
            queryset = TouristSpot.objects.filter(pk=id)

        if name:
            queryset = queryset.filter(name__iexact=name)
        
        if description:
            queryset = queryset.filter(description__iexact=description)

        return queryset

    # Executado na exibicao da lista de resultados
    def list(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).list(request, *args, **kwargs)

    # Executando quando um recurso vai ser criado
    def create(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).create(request, *args, **kwargs)

    # Executado quando um recurso vai ser deletado
    def destroy(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).destroy(request, *args, **kwargs)

    # Executado, assim como o LIST, quando o usuario pede para ver os
    # dados dos recursos, mas esse metodo e executado quando
    # quando eu quero obter um recurso em especifico e nao
    # a lista de todos os recursos presentes no banco
    def retrieve(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).retrieve(request, *args, **kwargs)

    # Executado quando um recurso vai ser atualizado por inteiro (PUT)
    def update(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).update(request, *args, **kwargs)

    # Executado quando apenas parte de um recurso vai ser atualizado (PATCH)
    def partial_update(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).par(request, *args, **kwargs)


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
