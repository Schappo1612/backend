from django.db import models



class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    claudio = models.ImageField(upload_to=(''), null=True, blank=True)

    def __str__(self):
        return self.descricao