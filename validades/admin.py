from django.contrib import admin
from .models import Validade

class ValidadeAdmin(admin.ModelAdmin):
    list_display = ('produto', 'estoque', 'dt_validade', 'dt_criacao',)
    list_filter = ('dt_validade', 'produto', 'dt_criacao',)
    search_fields = ('produto__nome',)

admin.site.register(Validade, ValidadeAdmin)