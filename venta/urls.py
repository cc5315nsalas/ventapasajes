from django.conf.urls import patterns, url

from venta import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^recorrido/(?P<id_recorrido>\d+)/$', views.detalle, name='detalle'),
    url(r'^buscar/$', views.buscar, name='buscar'),
    url(r'^confirmar/(?P<id_recorrido>\d+)/(?P<id_asiento>\d+)/$', views.confirmar, name='confirmar'),
    url(r'^vender/(?P<id_pasaje>\d+)/$', views.vender, name='vender'),
    url(r'^cambiar/$', views.cambiar, name='cambiar'),
    url(r'^cambiacion/$', views.cambiacion, name='cambiacion'),
    url(r'^cambiacion/(?P<id_pasaje>\d+)/$', views.do_cambiar, name='do_cambiar'),
    url(r'^devolver/$', views.devolver, name='devolver'),
    url(r'^devolucion/$', views.devolucion, name='devolucion'),
    url(r'^devolucion/(?P<id_pasaje>\d+)/$', views.do_devolver, name='do_devolver'),
)