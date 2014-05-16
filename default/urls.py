from django.conf.urls import patterns, url

from default import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page>[0-9]+)/$', views.index_page, name='index_page'),
)
