from django.conf.urls import include, url
from .views import  index, about, jugador, team, consultas, manager, teams


urlpatterns = [
	url(r'^$', index),
	url(r'^about/', about, name="about"),
	url(r'^home/', index, name="home"),
	url(r'^home/', index, name="BD"),
	url(r'^player/', jugador.as_view(), name="jugadores"),
	url(r'^managers/', manager.as_view(), name="managers"),
	url(r'^equipo/', teams.as_view(), name="equipo"),

	url(r'^consulta/(?P<query_id>[0-9]+)/', consultas, name="consultas"),
	url(r'^consulta/',consultas, name="consultas"),
	url(r'^index/', index)
]