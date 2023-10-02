from rest_framework.serializers import ModelSerializer

from academia.models import Categoria, Fornecedor, Produtos
from uploader.serializers import ImageSerializer

class CategoriaSerializer(ModelSerializer):
    imagem = ImageSerializer()
    class Meta:
        model = Categoria
        fields = "__all__"
