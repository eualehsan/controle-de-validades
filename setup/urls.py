from django.contrib import admin
from django.urls import path, include
from produtos import views as p_views
from usuarios import views as u_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', p_views.carrega_inicio, name='carrega_inicio'),
    path('inicio/', p_views.carrega_inicio, name='carrega_inicio'),
    path('erro/', p_views.exibe_erro, name="exibe_erro"),
    path('produtos/', include('produtos.urls')),
    path('categorias/', include('categorias.urls')),
    path('marcas/', include('marcas.urls')),
    path('validades/', include('validades.urls')),
    path('auth/', include('usuarios.urls')),
]
