#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


original_fields = ['playerID','awardID','yearID','lgID','tie','notes']

file1 = open('../../DatosOriginales/AwardsPlayers.csv', 'rb')
file2 = open('../../DatosOriginales/AwardsManagers.csv', 'rb')


reader1 = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)
reader2 = csv.DictReader(file2, delimiter=',', fieldnames=original_fields)


file3 = open('Awards.csv', 'wb')
fieldnames = original_fields + ['category']

writer = csv.DictWriter(file3, delimiter=',', fieldnames=fieldnames)
writer.writeheader()  

next(reader1)

for row in reader1:		
	new_row = {}
	new_row['playerID'] = row['playerID']
	new_row['awardID'] = row['awardID']
	new_row['yearID'] = row['yearID']
	new_row['lgID'] = row['lgID']
	new_row['tie'] = row['tie']
	new_row['notes'] = row['notes']
	
	new_row['category'] = "player"
	writer.writerow(new_row)
next(reader2)

for row in reader2:		
	new_row = {}
	new_row['playerID'] = row['playerID']
	new_row['awardID'] = row['awardID']
	new_row['yearID'] = row['yearID']
	new_row['lgID'] = row['lgID']
	new_row['tie'] = row['tie']
	new_row['notes'] = row['notes']
	
	new_row['category'] = "manager"
	writer.writerow(new_row)

file1.close() 
file2.close()
file3.close()