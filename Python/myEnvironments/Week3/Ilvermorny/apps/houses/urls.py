from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.new),
	url(r'^students$', views.index),
	url(r'^students/create', views.create),
	url(r'^students/(?P<info>.+)', views.show)
]
