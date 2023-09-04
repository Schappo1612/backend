from django.contrib import admin

from academia.models import Categoria, Fornecedor, Produtos

admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Produtos)