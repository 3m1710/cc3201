#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


file1 = open('../../DatosOriginales/Batting.csv', 'rb')

original_fields = ['playerID','yearID','stint','teamID','lgID','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)


file2 = open('Batting.csv', 'wb')
fieldnames = ['playerID','yearID','stint','teamID',#'lgID',
			  'G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP']

writer = csv.DictWriter(file2, delimiter=',', fieldnames=fieldnames)
writer.writeheader()  

next(reader)

for row in reader:		
	new_row = {}
	new_row['playerID'] = row['playerID']
	new_row['yearID'] = row['yearID']
	new_row['stint'] = row['stint']
	new_row['teamID'] = row['teamID']
	#new_row['lgID'] = row['lgID']
	new_row['G'] = row['G']
	new_row['AB'] = row['AB']
	new_row['R'] = row['R']
	new_row['H'] = row['H']
	new_row['2B'] = row['2B']
	new_row['3B'] = row['3B']
	new_row['HR'] = row['HR']
	new_row['RBI'] = row['RBI']
	new_row['SB'] = row['SB']
	new_row['CS'] = row['CS']
	new_row['BB'] = row['BB']
	new_row['SO'] = row['SO']
	new_row['IBB'] = row['IBB']
	new_row['HBP'] = row['HBP']
	new_row['SH'] = row['SH']
	new_row['SF'] = row['SF']
	new_row['GIDP'] = row['GIDP']
	writer.writerow(new_row)

file1.close() 
file2.close()