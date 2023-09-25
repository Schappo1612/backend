from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    # email = models.EmailField()
    claudio = models.ImageField(upload_to=(''), null=True, blank=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Fornecedores"