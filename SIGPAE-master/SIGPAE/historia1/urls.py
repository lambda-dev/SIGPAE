from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.model_form_upload, name='model_form_upload'),
    url(r'^a$',views.editar,name='editar'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
