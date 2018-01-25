from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^send_data$', views.send_data),
	url(r'^success$', views.success)
]