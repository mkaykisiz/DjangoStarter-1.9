from user import views

__author__ = 'mehmet'

from django.conf.urls import patterns, url

urlpatterns = (
    url(r'^$', views.index, name='index'),
   # url(r'^content/(?P<content_id>[0-9]+)/$', views.contact_detail),
)
