from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='blog_list'),
    url(r'^(?P<blog_id>\d+)/$', views.detail, name='blog_detail'),
)