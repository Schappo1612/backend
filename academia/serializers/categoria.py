from rest_framework.serializers import ModelSerializer

from academia.models import Categoria, Fornecedor, Produtos

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
