from django.urls import path
from ventas import views

app_name = 'ventas'

urlpatterns = [
    path('nueva_venta', views.nueva_venta, name='nueva_venta'),
    path('pagar', views.pagar, name='pagar'),
    path('listar_ventas', views.listar_ventas, name='listar_ventas'),
]