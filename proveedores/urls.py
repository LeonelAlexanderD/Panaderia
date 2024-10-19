from django.urls import path
from proveedores import views

app_name = 'proveedores'

urlpatterns = [
    path('cargar_proveedor', views.alta_proveedor, name='cargar_proveedor'),
    path('listar_proveedor', views.listar_proveedor, name='listar_proveedor'),
    path('nuevo_pedido', views.nuevo_pedido, name='nuevo_pedido'),
    path('listar_pedidos', views.listar_pedidos, name='listar_pedidos'),
    path('nueva_recepcion', views.nueva_recepcion, name='nueva_recepcion'),
    path('listar_recepciones', views.listar_recepciones, name='listar_recepciones'),
]