#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


file1 = open('../../DatosOriginales/Managers.csv', 'rb')

original_fields = ['playerID','yearID','teamID','lgID','inseason','G','W','L','rank','plyrMgr']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)


file2 = open('Managers.csv', 'wb')
fieldnames = ['playerID','yearID','teamID',#'lgID',
			  'inseason','G','W','L']#,'rank','plyrMgr']

writer = csv.DictWriter(file2, delimiter=',', fieldnames=fieldnames)
writer.writeheader()  

next(reader)
for row in reader:		
	new_row = {}
	new_row['playerID'] = row['playerID']
	new_row['yearID'] = row['yearID']
	new_row['teamID'] = row['teamID']
	#new_row['lgID'] = row['lgID']
	new_row['inseason'] = row['inseason']
	new_row['G'] = row['G']
	new_row['W'] = row['W']
	new_row['L'] = row['L']
	# new_row['rank'] = row['rank']
	# new_row['plyrMgr'] = row['plyrMgr']
	
	writer.writerow(new_row)

file1.close() 
file2.close()