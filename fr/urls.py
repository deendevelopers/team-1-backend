from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mosques/$', views.mosques_list, name='mosques_list'),
    url(r'^mosques/(?P<mosque_id>\d+)/$', views.mosques_detail, name='mosques_detail'),
    
]