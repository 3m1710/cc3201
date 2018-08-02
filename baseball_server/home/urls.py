from django.conf.urls import include, url
from .views import  index, about


urlpatterns = [
	url(r'^$', index),
	url(r'^about/', about, name="about"),
	url(r'^home/', index, name="home"),
	url(r'^index/', index)
]