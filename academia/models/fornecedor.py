from django.db import models
from uploader.models import Image

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    # email = models.EmailField()
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Fornecedores"