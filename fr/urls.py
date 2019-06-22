from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mosques/$', views.mosques, name='mosques'),
    
]