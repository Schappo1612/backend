from rest_framework.viewsets import ModelViewSet

from academia.models import Categoria
from academia.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
