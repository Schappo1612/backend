from django.db import models
from academia.models import Categoria,Fornecedor

class Produtos(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="produtos")
    Fornecedor = models.ManyToManyField(Fornecedor, related_name="produtos")

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"