from rest_framework.serializers import ModelSerializer

from academia.models import Categoria, Fornecedor, Produtos

class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = "__all__"
