from django.conf.urls import include, url
from .views import  index, about, jugador, team


urlpatterns = [
	url(r'^$', index),
	url(r'^about/', about, name="about"),
	url(r'^home/', index, name="home"),
	url(r'^home/', index, name="BD"),
	url(r'^player/', jugador.as_view(), name="jugadores"),
	url(r'^player/', team, name="teams"),
	url(r'^index/', index)
]