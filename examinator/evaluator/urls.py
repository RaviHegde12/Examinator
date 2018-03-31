from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^file_upload/$', views.model_form_upload, name='file_upload'),
    url(r'^generate/$', views.generate, name='generate'),
]
