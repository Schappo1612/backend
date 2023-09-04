from rest_framework.serializers import ModelSerializer

from academia.models import Categoria, Fornecedor, Produtos

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = "__all__"
        depth = 1

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = "__all__"
        depth = 1

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
