#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


file1 = open('../../DatosOriginales/Teams.csv', 'rb')

original_fields = ['yearID','lgID','teamID','franchID','divID','Rank','G','GHome','W','L','DivWin','WCWin','LgWin','WSWin','R','AB','H','2B','3B','HR','BB','SO','SB','CS','HBP','SF','RA','ER','ERA','CG','SHO','SV','IPOuts','HA','HRA','BBA','SOA','E','DP','FP','name','park','attendance','BPF','PPF']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)


file2 = open('Teams2.csv', 'wb')
fieldnames = ["teamID","name", "season_debut",# "franchID", 
			  "franchName"]
writer = csv.DictWriter(file2, delimiter=',', fieldnames=fieldnames)
writer.writeheader()  
lista = []


file3 = open('../../DatosOriginales/TeamsFranchises.csv', 'rb')
fieldnames3 = ["franchID","franchName","active","NAassoc"]
reader3 = csv.DictReader(file3, delimiter=',', fieldnames=fieldnames3)


next(reader)
next(reader3)

frachises = {}
for row in reader3:
	frachises[row["franchID"]] = row["franchName"]

for row in reader:		
	new_row ={}

	if not [row["teamID"], row["franchID"], row["name"]] in lista:
		lista.append([row["teamID"], row["franchID"], row["name"]])

		new_row["teamID"] = row["teamID"]
		new_row["name"] = 	row["name"]	
		#new_row["franchID"] = row["franchID"]		
		new_row["season_debut"]  = row["yearID"]		
		new_row["franchName"] = frachises[row["franchID"]] 		
		writer.writerow(new_row)

file1.close() 
file2.close()