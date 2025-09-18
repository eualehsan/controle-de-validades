from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_categorias, name='lista_categorias'),
    path('cadastar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('edita_catgoria/<int:id>', views.editar_categoria, name='editar_categoria'),
    path('deleta_categoria/<int:id>', views.deleta_categoria, name='deleta_categoria'),
]