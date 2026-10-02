from django.urls import path
from . import views

urlpatterns = [
    path('', views.sesion_lista, name='sesion_lista'),
    path('nueva/', views.sesion_crear, name='sesion_crear'),
    path('<int:pk>/', views.sesion_detalle, name='sesion_detalle'),
    path('<int:pk>/editar/', views.sesion_editar, name='sesion_editar'),
    path('<int:pk>/eliminar/', views.sesion_eliminar, name='sesion_eliminar'),
]