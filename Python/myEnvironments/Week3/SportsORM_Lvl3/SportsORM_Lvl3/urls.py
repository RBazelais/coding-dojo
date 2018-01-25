from django.conf.urls import url, include 
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.sports_ORM_3.urls')) 
]