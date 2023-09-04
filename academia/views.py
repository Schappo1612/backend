from rest_framework.viewsets import ModelViewSet

from academia.models import Categoria, Fornecedor
from academia.serializers import CategoriaSerializer, FornecedorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FornecedorViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer