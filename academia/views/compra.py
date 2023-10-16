from rest_framework.viewsets import ModelViewSet

from academia.models import Compra
from academia.serializers import CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer