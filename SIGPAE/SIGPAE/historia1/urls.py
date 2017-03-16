from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^upload/$', views.model_form_upload, name='model_form_upload'),
    url(r'^editar/(?P<pk>\d+)$', views.editar_t, name='editar_t'),
    url(r'^datospasa/(?P<pk>\d+)$', views.form_pasa, name='form_pasa'),
    url(r'^consultar/$', views.buscar, name='buscar'),
    url(r'^consultar/p$', views.buscar_p, name='buscar_p'),
    url(r'^consultar/t$', views.buscar_t, name='buscar_t'),
    url(r'^consultar/s$', views.buscar_s, name='buscar_s'),
    url(r'^consultar/view/(?P<pk>\d+)$', views.view_p, name='view_p'),
    url(r'^consultar/pasa/(?P<pk>\d+)$', views.view_s, name='view_s'),
    url(r'^$', views.index, name='index'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
