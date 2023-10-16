from rest_framework.viewsets import ModelViewSet

from academia.models import  Produtos
from academia.serializers import ProdutoSerializer


class ProdutosViewSet(ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer