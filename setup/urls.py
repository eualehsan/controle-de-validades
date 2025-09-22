from django.contrib import admin
from django.urls import path, include
from produtos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.carrega_inicio, name='carrega_inicio'),
    path("erro/", views.exibe_erro, name="exibe_erro"),
    path('produtos/', include('produtos.urls')),
    path('categorias/', include('categorias.urls')),
    path('marcas/', include('marcas.urls')),
    path('validades/', include('validades.urls')),
    path('auth/', include('usuarios.urls')),
]
