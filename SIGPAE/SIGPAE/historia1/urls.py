# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^upload/$', views.model_form_upload, name='model_form_upload'),
    url(r'^editar/(?P<pk>\d+)$', views.editar_t, name='editar_t'),
    url(r'^datospasa/(?P<pk>\d+)$', views.form_pasa, name='form_pasa'),
    url(r'^consultar/p$', views.buscar_p, name='buscar_p'),
    url(r'^consultar/t$', views.buscar_t, name='buscar_t'),
    url(r'^consultar/s$', views.buscar_s, name='buscar_s'),
    url(r'^consultar/view/(?P<pk>\d+)$', views.view_p, name='view_p'),
    url(r'^consultar/pasa/(?P<pk>\d+)$', views.view_s, name='view_s'),
    url(r'^reportes/global/', views.r_global, name='r_global'),
    url(r'^editar/referencias/(?P<pk>\d+)$', views.referencias, name='referencias'),
    url(r'^add/referencias/(?P<pk>\d+)$', views.add_ref, name='add_ref'),
    url(r'^add/referencias/extra/(?P<pkD>(\d+))/(?P<pkR>(\d+))/$', views.add_extra, name='add_extra'),
    url(r'^referencias/autor/(?P<pkD>(\d+))/(?P<pkR>(\d+))/$', views.add_autores, name='add_autores'),
    url(r'^referencias/campos_extra/(?P<pkD>(\d+))/(?P<pkR>(\d+))/$', views.add_extras, name='add_extras'),
    url(r'^$', views.index, name='index'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
