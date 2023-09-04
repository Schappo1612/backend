from rest_framework.viewsets import ModelViewSet

from academia.models import  Fornecedor
from academia.serializers import FornecedorSerializer


class FornecedorViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer