from django.conf.urls import patterns, url

from member import views

urlpatterns = patterns('',
    url(r'^login/$', views.my_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.my_logout, name='logout'),
    url(r'^city_list/$', views.city_list_with_region, name='city_list'),
)
