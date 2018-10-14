#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


file1 = open('../../DatosOriginales/Pitching.csv', 'rb')

original_fields = ['playerID','yearID','stint','teamID','lgID','W','L','G','GS','CG','SHO','SV','IPouts','H','ER','HR','BB','SO','BAOpp','ERA','IBB','WP','HBP','BK','BFP','GF','R','SH','SF','GIDP']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)


file2 = open('Pitching.csv', 'wb')
fieldnames = ['playerID','yearID','stint','teamID',#'lgID',
			  'W','L','G','GS','CG','SHO','SV','IPouts','H','ER','HR','BB','SO','BAOpp','ERA','IBB','WP','HBP','BK','BFP','GF','R','SH','SF','GIDP']
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
	new_row['W'] = row['W']
	new_row['L'] = row['L']
	new_row['G'] = row['G']
	new_row['GS'] = row['GS']
	new_row['CG'] = row['CG']
	new_row['SHO'] = row['SHO']
	new_row['SV'] = row['SV']
	new_row['IPouts'] = row['IPouts']
	new_row['H'] = row['H']
	new_row['ER'] = row['ER']
	new_row['HR'] = row['HR']
	new_row['BB'] = row['BB']
	new_row['SO'] = row['SO']
	new_row['BAOpp'] = row['BAOpp']
	new_row['ERA'] = row['ERA']
	new_row['IBB'] = row['IBB']
	new_row['WP'] = row['WP']
	new_row['HBP'] = row['HBP']
	new_row['BK'] = row['BK']
	new_row['BFP'] = row['BFP']
	new_row['GF'] = row['GF']
	new_row['R'] = row['R']
	new_row['SH'] = row['SH']
	new_row['SF'] = row['SF']
	new_row['GIDP'] = row['GIDP']



	writer.writerow(new_row)

file1.close() 
file2.close()