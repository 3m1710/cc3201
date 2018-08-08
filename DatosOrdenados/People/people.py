#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


paises = {'D.R.': 'Dominican Republic', 'CAN': 'Canada', 'P.R.':'Puerto Rico'}

file1 = open('../People.csv', 'rb')

original_fields = ['playerID', 'birthYear', 'birthMonth','birthDay','birthCountry','birthState','birthCity','deathYear','deathMonth','deathDay','deathCountry','deathState','deathCity','nameFirst','nameLast','nameGiven','weight','height','bats','throws','debut','finalGame','retroID','bbrefID']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)

file2 = open('People.csv', 'wb')
fieldnames = ['personID', 'givenName','lastName','birthDate', 'birthCountry', 'birthState', 'birthCity', 'deathDate','deathCountry', 'deathState','deathCity', 'height','weight','bats','throws', 'debut','finalGame']

writer = csv.DictWriter(file2, delimiter=',', fieldnames=fieldnames)
writer.writeheader()  
next(reader)

for row in reader:
	new_row = {}

	new_row['personID']  = row['playerID']
	new_row['givenName'] = row['nameGiven']
	new_row['lastName']  = row['nameLast']	
	new_row['birthState'] 	= row['birthState']
	new_row['birthCity'] 	= row['birthCity']
	new_row['deathState'] 	= row['deathState']
	new_row['deathCity']	= row['deathCity']

	if row['weight']:
		new_row['weight'] =  "{0:.2f}".format(float(row['weight'])*0.453592)
	else:
		new_row['weight'] = ""

	if row['height']:
		new_row['height'] = str(int(float(row['height'])*2.54))
	else:
		new_row['height'] = ""

	new_row['bats']	  = row['bats']
	new_row['throws'] = row['throws']
	new_row['debut']  = row['debut']
	new_row['finalGame'] =  row['finalGame']


	if row['birthCountry'] in paises:
		new_row['birthCountry'] = paises[row['birthCountry']]
	else:
		new_row['birthCountry'] = row['birthCountry']

	if row['deathCountry'] in paises:
		new_row['deathCountry'] = paises[row['deathCountry']]
	else:
		new_row['deathCountry'] = row['deathCountry']


	if row['birthYear']:
		new_row['birthDate'] =  row['birthYear'] + "-" + row['birthMonth'] + "-" + row['birthDay'] 
	else:
		new_row['birthDate'] = ""
	
	if row['deathYear']:
		new_row['deathDate'] =  row['deathYear'] + "-" + row['deathMonth'] + "-" + row['deathDay'] 
	else:
		new_row['deathDate'] = ""

	writer.writerow(new_row)

file1.close()   # <---IMPORTANT

# Do the writing
file2.close()