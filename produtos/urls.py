from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('cadastrar_produtos/', views.cadastrar_produto, name='cadastrar_produto'),
    path('edita_produto/<int:id>', views.edita_produto, name='edita_produto'),
    path('deleta_produto/<int:id>', views.deleta_produto, name='deleta_produto'),
    path('deleta_todos_produtos/', views.deleta_todos_produtos, name='deleta_todos_produtos'),
]