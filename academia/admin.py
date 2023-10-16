from django.contrib import admin

from academia.models import Categoria, Fornecedor, Produtos, Compra, ItensCompra

class ItensCompraInline(admin.TabularInline):
    model = ItensCompra

admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Produtos)

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]