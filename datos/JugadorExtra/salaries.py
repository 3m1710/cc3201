#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


file1 = open('../../DatosOriginales/Salaries.csv', 'rb')

original_fields = ['yearID','teamID','lgID','playerID','salary']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)


file2 = open('Salaries.csv', 'wb')
fieldnames = ['yearID','teamID',#'lgID',
				   'playerID','salary']

writer = csv.DictWriter(file2, delimiter=',', fieldnames=fieldnames)
writer.writeheader()  

next(reader)

for row in reader:		
	new_row = {}

	new_row['yearID'] = row['yearID']
	new_row['teamID'] = row['teamID']
	#new_row['lgID'] = row['lgID']
	new_row['playerID'] = row['playerID']
	new_row['salary'] = row['salary']
	writer.writerow(new_row)

file1.close() 
file2.close()