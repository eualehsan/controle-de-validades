from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_marcas, name='lista_marcas'),
    path('cadastrar_marca/', views.cadastra_marca, name='cadastra_marca'),
    path('atualiza_marca/<int:id>', views.atualiza_marca, name='atualiza_marca'),
    path('deleta_marca/<int:id>', views.deleta_marca, name='deleta_marca')
]
