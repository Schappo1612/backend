from rest_framework.serializers import ModelSerializer, CharField
from uploader.serializers import ImageSerializer
from academia.models import Categoria, Fornecedor, Produtos

class FornecedorSerializer(ModelSerializer):
    # imagem = CharField(source="imagem.file", read_only = True)
    class Meta:
        model = Fornecedor
        fields = ["id", "nome", "imagem"]
        depth = 1
