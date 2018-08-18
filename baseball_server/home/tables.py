#!/usr/bin/env python
# -*- coding: utf-8 -*-
import django_tables2 as tables
from django_tables2 import RequestConfig



class TablaJugador(tables.Table):
    #name = tables.Column()
    peopleid = tables.Column("ID")
    lastname = tables.Column()
    givenname = tables.Column()
    
    birthdate = tables.Column()
    birthcountry = tables.Column()
    height = tables.Column()
    weight = tables.Column()
    throws = tables.Column(orderable=False)
    bats = tables.Column(orderable=False)
    
    debut = tables.Column()
    finalgame = tables.Column()

    class Meta:
        attrs = {"class": "paleblue"} 


def TableFactory(data):
    dics = {}
    for key in data.keys():
        dics[key] = tables.Column()

    return type('TablaGenerada', (tables.Table,), dics)
