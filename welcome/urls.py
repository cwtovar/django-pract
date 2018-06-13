from django.conf.urls import url
from . import views

urlpatters = [url(r'^$', views.view1, name='view1'),]
