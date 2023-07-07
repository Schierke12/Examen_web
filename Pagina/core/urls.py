from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView
from .views import ProductosPorCategoriaListView

urlpatterns = [
    path('', home, name='home'),
    path('login', LoginView.as_view(template_name="core/login.html"), name='login'),
    path("logout", logout, name="logout"),
    path('perfil', historial, name='perfil'),
    path('registro', registro, name='registro'),
    path('realizarCompra', realizarCompra, name='realizarCompra'),
    path('descripcion/<codigo>', descripcion, name='descripcion'),
    path('limpiar', limpiar),
    path('carroCompras/<codigo>', carroCompras, name='carroCompras'),
    path('limpiarCarro/<codigo>', limpiarCarro, name='limpiarCarro'),
    path('carro', carro, name='carro'),
    path('productos/gatos/', ProductosPorCategoriaListView.as_view(), {'categoria': 'gatos'}, name='productos_gatos'),
    path('productos/perros/', ProductosPorCategoriaListView.as_view(), {'categoria': 'perros'}, name='productos_perros'),
    path('productos/ratas/', ProductosPorCategoriaListView.as_view(), {'categoria': 'ratas'}, name='productos_ratas'),
    path('productos/aves/', ProductosPorCategoriaListView.as_view(), {'categoria': 'aves'}, name='productos_aves'),
    path('suscribir', suscribir, name="suscribir"),
]

