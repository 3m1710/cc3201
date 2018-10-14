#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


file1 = open('../../DatosOriginales/Teams.csv', 'rb')

original_fields = ['yearID','lgID','teamID','franchID','divID','Rank','G','GHome','W','L','DivWin','WCWin','LgWin','WSWin','R','AB','H','2B','3B','HR','BB','SO','SB','CS','HBP','SF','RA','ER','ERA','CG','SHO','SV','IPOuts','HA','HRA','BBA','SOA','E','DP','FP','name','park','attendance','BPF','PPF']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)


file2 = open('Season.csv', 'wb')
fieldnames = [ 'year', 'league',  'division',  'division_winner']
writer = csv.DictWriter(file2, delimiter=',', fieldnames=fieldnames)
writer.writeheader()  
lista = []


file3 = open('PostSeason.csv', 'wb')
fieldnames3 = [ 'year', 'league',  'league_champion',  'ws_champion']
writer2 = csv.DictWriter(file3, delimiter=',', fieldnames=fieldnames3)
writer2.writeheader()  


next(reader)



for row in reader:		
	new_row ={}
	new_row2 ={}

	if row["DivWin"] == "Y":
		new_row['year'] = row["yearID"]
		new_row['league'] = row["lgID"]
		new_row['division'] = row["divID"]
		new_row['division_winner'] = row["teamID"]
		writer.writerow(new_row)

	if row["LgWin"] == "Y":
		new_row2['year'] = row["yearID"]
		new_row2['league'] = row["lgID"]
		new_row2['league_champion'] = row["teamID"]
		new_row2['ws_champion'] = row["WSWin"]
		writer2.writerow(new_row2)


file1.close() 
file2.close()
file3.close()