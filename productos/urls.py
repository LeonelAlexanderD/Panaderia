from django.urls import path
from productos import views

app_name = 'estudiante'

urlpatterns = [
    path('listar_insumos', views.listar_insumos, name='listar_insumos'),
    path('cargar_insumo', views.cargar_insumo, name='cargar_insumo'),
    path('listar_productos', views.listar_productos, name='listar_productos'),
    path('cargar_producto', views.cargar_producto, name='cargar_producto'),
]