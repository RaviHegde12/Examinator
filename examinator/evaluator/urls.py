from . import views
from django.conf.urls import url
from . import word_net
from . import word2vec


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^file_upload/(?P<file_id>[0-9]+)$', views.model_form_upload, name='file_upload'),
    url(r'^process/$', views.process, name='process'),
    url(r'^show_content/$', views.show_content, name='show_content'),
    url(r'^generate/$', views.generate, name='generate'),
    url(r'^report/$', views.generate_report, name='generateReport'),
    url(r'^word_net/$', word_net.process, name='word_net'),
    url(r'^word2vec/$', word2vec.word2vec, name='word2vec'),
]
