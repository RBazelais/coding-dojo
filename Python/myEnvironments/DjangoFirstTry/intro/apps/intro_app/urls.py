from django.conf.urls import url
from . import views  


urlpatterns = [
    url(r'^$', views.index),
    url(r'^new', views.new),
    url(r'^create', views.create),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit), #Look this and then store this int
    url(r'^(?P<number>\d+)/delete$', views.destroy),
]
