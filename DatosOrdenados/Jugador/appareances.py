#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


file1 = open('../../DatosOriginales/Appearances.csv', 'rb')

original_fields = ['yearID','teamID','lgID','playerID','G_all','GS','G_batting','G_defense','G_p','G_c','G_1b','G_2b','G_3b','G_ss','G_lf','G_cf','G_r']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)


file2 = open('Appearances.csv', 'wb')
fieldnames = ['yearID','teamID',#'lgID',
			  'playerID','G_all','GS','G_batting','G_defense','G_p','G_c','G_1b','G_2b','G_3b','G_ss','G_lf','G_cf','G_r']
writer = csv.DictWriter(file2, delimiter=',', fieldnames=fieldnames)
writer.writeheader()  

next(reader)
for row in reader:		
	new_row = {}
	new_row['yearID'] = row['yearID']
	new_row['teamID'] = row['teamID']
	#new_row['lgID'] = row['lgID']
	new_row['playerID'] = row['playerID']
	new_row['G_all'] = row['G_all']
	new_row['GS'] = row['GS']
	new_row['G_batting'] = row['G_batting']
	new_row['G_defense'] = row['G_defense']
	new_row['G_p'] = row['G_p']
	new_row['G_c'] = row['G_c']
	new_row['G_1b'] = row['G_1b']
	new_row['G_2b'] = row['G_2b']
	new_row['G_3b'] = row['G_3b']
	new_row['G_ss'] = row['G_ss']
	new_row['G_lf'] = row['G_lf']
	new_row['G_cf'] = row['G_cf']
	new_row['G_r'] = row['G_r']
	
	writer.writerow(new_row)

file1.close() 
file2.close()