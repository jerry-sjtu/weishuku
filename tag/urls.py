from django.conf.urls import patterns, url

from tag import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^taglist/$', views.tag_list, name='taglist'),
    url(r'^tb/(?P<tag_id>\d+)/$', views.taged_book, name='taged_book'),
)
