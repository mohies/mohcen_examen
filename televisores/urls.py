from django.urls import path, re_path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ultimo_voto/<int:televisor_id>',views.voto,name='ultimo_voto'),
    path('votos_bajos/<int:usuario_id>/', views.televisores_con_voto_bajo, name='televisores_con_voto_bajo'),
    path('televisores_bajos/<int:usuario_id>/', views.televisores_con_voto_bajo, name='televisores_con_voto_bajo'),
    path('usuarios_no/', views.usuarios_no, name='usuarios_no'),
    path('cuentas-bancarias-juan/', views.cuentas_bancarias_juan, name='cuentas_bancarias_juan'),
    path('votosfiltrados/', views.votos_filtrados, name='votos_filtrados'),
    path('media/', views.media, name='media'),
    

]