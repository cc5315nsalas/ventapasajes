from django.conf.urls import patterns, url

from compra import views

urlpatterns = patterns('',
    url(r'^$', views.indice, name='indice'),
    url(r'^recorridoC/(?P<id_recorrido>\d+)/$', views.detalleC, name='detalleC'),
    url(r'^buscarC/$', views.buscarC, name='buscarC'),
    url(r'^confirmarC/(?P<id_recorrido>\d+)/(?P<sid_pasaje>[A-Fa-f0-9]+)/$', views.confirmarC, name='confirmarC'),
    url(r'^comprar/(?P<sid_pasaje>[A-Fa-f0-9]+)/$', views.comprar, name='comprar'),

)