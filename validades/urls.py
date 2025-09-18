from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_validades, name='lista_validades'),
    path('cadastrar_validade/', views.cadastrar_validade, name='cadastrar_validade'),
    path('edita_validade/<int:id>', views.edita_validade, name='edita_validade'),
    path('deleta_validade/<int:id>', views.deleta_validade, name='deleta_validade'),
]
