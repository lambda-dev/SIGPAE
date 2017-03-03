from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^upload/$', views.model_form_upload, name='model_form_upload'),
    url(r'^editar/$', views.editar_t, name='editar_t'),
    url(r'^consultar/$', views.buscar, name='buscar'),
    url(r'^$', views.index, name='index'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
