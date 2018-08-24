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


ligas_choice = [
     ("AL","American League"),
     ("NL","National League"),
     ("NA", "NA (Liga vieja)" ),
     ("FL", "FL (Liga vieja)" ),
     ("UA", "UA (Liga vieja)" ),
     ("PL", "PL (Liga vieja)" ),
     ("AA", "AA (Liga vieja)" )
]
class Jugador(forms.Form):
    nombre = forms.CharField(label='1er Nombre', max_length=100, required=False)
    nombre2 = forms.CharField(label='2do Nombre', max_length=100, required=False)
    apellido = forms.CharField(label='Apellido', max_length=100, required=False)
    ordenar = forms.ChoiceField(label="Ordenar por ", widget=forms.Select,choices=order_choice)
    #temporada = forms.CharField(label='Temporada', max_length=100)


class consulta5(forms.Form):
    league = forms.ChoiceField(label="Liga ", widget=forms.Select,choices=ligas_choice)
    #temporada = forms.CharField(label='Temporada', max_length=100)



class consulta1(forms.Form):
    nombre = forms.CharField(label='Nombre(s)', max_length=100, required=True)
    #nombre2 = forms.CharField(label='2do Nombre', max_length=100, required=True)
    apellido = forms.CharField(label='Apellido', max_length=100, required=True)
    # playerid = forms.CharField(label='ID Jugador', max_length=100, required=False)
    #ordenar = forms.ChoiceField(label="Ordenar por ", widget=forms.Select,choices=order_choice)
    #temporada = forms.CharField(label='Temporada', max_length=100)
    # def clean(self):
    #     cleaned_data = super(consulta1, self).clean()
    #     _apellido = cleaned_data.get("apellido")
    #     _id = cleaned_data.get("playerid")
    #     if not _apellido and not _id: 
    #         msg = forms.ValidationError("Se necesita o Apellido o ID del jugador para la búsqueda.")
    #         self.add_error('apellido', msg)
    #         self.add_error('ID', msg)
    #         raise msg
    #     return cleaned_data


class consulta2(forms.Form):
    equipo = forms.CharField(label='Nombre de Equipo', max_length=100, required=True)
    #nombre2 = forms.CharField(label='2do Nombre', max_length=100, required=True)

class Teams(forms.Form):
    team_name = forms.CharField(label='Nombre', max_length=100, required=False)
    teamid = forms.CharField(label='ID', max_length=100, required=False)
