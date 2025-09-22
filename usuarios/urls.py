from django.urls import path
from . import views

urlpatterns = [
    path('cadastar/', views.cadastra_usuario, name='cadastra_usuario'),
    path('login/', views.loga_usuario, name='loga_usuario'),
]
