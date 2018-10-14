#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


file1 = open('../../DatosOriginales/Fielding.csv', 'rb')

original_fields = ['playerID','yearID','stint','teamID','lgID','POS','G','GS','InnOuts','PO','A','E','DP','PB','WP','SB','CS','ZR']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)


file2 = open('Fielding.csv', 'wb')
fieldnames = ['playerID','yearID','stint','teamID',#'lgID',
			  'POS','G','GS','InnOuts','PO','A','E','DP','PB','WP','SB','CS','ZR']

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
	new_row['POS'] = row['POS']
	new_row['G'] = row['G']
	new_row['GS'] = row['GS']
	new_row['InnOuts'] = row['InnOuts']
	new_row['PO'] = row['PO']
	new_row['A'] = row['A']
	new_row['E'] = row['E']
	new_row['DP'] = row['DP']
	new_row['PB'] = row['PB']
	new_row['WP'] = row['WP']
	new_row['SB'] = row['SB']
	new_row['CS'] = row['CS']
	new_row['ZR'] = row['ZR']
	writer.writerow(new_row)

file1.close() 
file2.close()