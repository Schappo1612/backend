from django.db import models

from usuario.models import Usuario
from academia.models import Categoria

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = (1,"Carrinho",)
        REALIZADO = (2,"Realizado",)
        PAGO = (3,"Pago",)
        ENTREGUE = (4,"Entregue",)

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras", blank = True, null = True)
    status = models.IntegerField(choices=StatusCompra.choices,  default=StatusCompra.CARRINHO, blank = True, null = True)

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens", blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)