from django.contrib import admin
from .models import Produto
from validades.models import Validade

class ValidadeInline(admin.TabularInline):
    model = Validade
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo_barras','descricao', 'categoria', 'marca',)   
    search_fields = ('descricao',)
    list_filter = ('categoria', 'marca',)
    inlines = [ValidadeInline]

admin.site.register(Produto, ProdutoAdmin)

