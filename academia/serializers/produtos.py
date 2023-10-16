from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer
from academia.models import Categoria, Fornecedor, Produtos

class ProdutoSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Produtos
        fields = "__all__"
        depth = 1

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = "__all__"
        depth = 1
    capa = ImageSerializer(required=False)

class ProdutoViewSet(ModelSerializer):
# ModelViewSet
    queryset = Produtos.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer

class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = ["id", "titulo", "preco"]
