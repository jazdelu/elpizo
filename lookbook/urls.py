from django.conf.urls import patterns, url

from lookbook import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='lookbook_list'),
    url(r'^(?P<lookbook_id>\d+)/$', views.detail, name='lookbook_detail'),
)