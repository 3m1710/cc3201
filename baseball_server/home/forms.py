#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import forms



order_choice = [
	("peopleid","Id"),
	( "lastname","apellido"),
	("givenname","nombres"),
	("birthdate","fecha de nacimiento"),
	("debut","debut")

]

class Jugador(forms.Form):
    nombre = forms.CharField(label='1er Nombre', max_length=100, required=False)
    nombre2 = forms.CharField(label='2do Nombre', max_length=100, required=False)
    apellido = forms.CharField(label='Apellido', max_length=100, required=True)
    ordenar = forms.ChoiceField(label="Ordenar por ", widget=forms.Select,choices=order_choice)
    #temporada = forms.CharField(label='Temporada', max_length=100)