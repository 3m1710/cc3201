#!/usr/bin/env python
# -*- coding: utf-8 -*-
import django_tables2 as tables
from django_tables2 import RequestConfig



class TablaJugador(tables.Table):
    #name = tables.Column()
    peopleid = tables.Column("ID")
    last_name = tables.Column()
    given_name = tables.Column()
    
    birthdate = tables.Column()
    birth_country = tables.Column()
    height = tables.Column()
    weight = tables.Column()
    throws = tables.Column(orderable=False)
    bats = tables.Column(orderable=False)
    
    debut = tables.Column()
    final_game = tables.Column()

    class Meta:
        attrs = {"class": "paleblue"} 

class TablaManager(tables.Table):
    #name = tables.Column()
    peopleid = tables.Column("ID")
    last_name = tables.Column("Apellido")
    given_name = tables.Column("Nombre(s)")
    
    birthdate = tables.Column("Nacimiento")
    birth_country = tables.Column("Lugar de Nacimiento")
    #height = tables.Column()
    #weight = tables.Column()
    #throws = tables.Column(orderable=False)
    #bats = tables.Column(orderable=False)
    
    debut = tables.Column(" Debut como Jugador ")
    man_debut = tables.Column(" Debut como Manager ")
    
    #final_game = tables.Column()

    class Meta:
        attrs = {"class": "paleblue"} 

class Tabla1(tables.Table):
    playerid = tables.Column("Player ID")
    given_name = tables.Column("Nombre")
    last_name = tables.Column("Apellido")
    teamid = tables.Column("Equipo ID")
    team_name = tables.Column("Equipo")
    primera_temporada = tables.Column("desde temporada")
    ultima_temporada = tables.Column("hasta temporada")
    
    class Meta:
        attrs = {"class": "paleblue"} 

class Tabla2(tables.Table):
    #name = tables.Column()

    team_name = tables.Column("Equipo")
    year = tables.Column("Año")
    given_name = tables.Column("Nombre")
    last_name = tables.Column("Apellido")
    salary = tables.Column("Salario")

    class Meta:
        attrs = {"class": "paleblue"} 


class Tabla3(tables.Table):
    #name = tables.Column()

    team_name = tables.Column("Equipo")
    year = tables.Column("Año")
    desempeno = tables.Column("Desempeño")

    class Meta:
        attrs = {"class": "paleblue"} 


class Teams(tables.Table):
    #name = tables.Column()
    teamid = tables.Column("Sigla")
    team_name = tables.Column("Nombre Equipo")
    franchise_name = tables.Column("Nombre Franquicia")
    season_debut = tables.Column("Debut en MLB")
    last_season = tables.Column("Ultima temporada en MLB")

    class Meta:
        attrs = {"class": "paleblue"} 



def TableFactory(data):
    dics = {}
    for key in data.keys():
        dics[key] = tables.Column()
    return type('TablaGenerada', (tables.Table,), dics)
