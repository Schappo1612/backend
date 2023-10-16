from django.db import models

from uploader.models import Image

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    imagem = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True, default=None)

    def __str__(self):
        return self.descricao