#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


file1 = open('Teams.csv', 'rb')

original_fields = ['yearID','lgID','teamID','franchID','divID','Rank','G','GHome','W','L','DivWin','WCWin','LgWin','WSWin','R','AB','H','2B','3B','HR','BB','SO','SB','CS','HBP','SF','RA','ER','ERA','CG','SHO','SV','IPOuts','HA','HRA','BBA','SOA','E','DP','FP','name','park','attendance','BPF','PPF']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)

Teams = {}
next(reader)
for row in reader:		
	if row['teamID'] in Teams:
		if row['lgID']!= Teams[row['teamID']][0]:
			print("Team =|=> Liga: {0} - {1}  - {2}".format(row['teamID'], Teams[row['teamID']][0], row['lgID'] ))

		if row['franchID'] != Teams[row['teamID']][1]:
			print("Team =|=> Franch: {0} - {1}  - {2}".format(row['teamID'], Teams[row['teamID']][1], row['franchID'] ))

		if row['divID'] != Teams[row['teamID']][2]:
			if Teams[row['teamID']][2] == "":
				Teams[row['teamID']][2] = row['divID']
			else:
				print("Team =|=> Div: {0} - {1}  - {2}".format(row['teamID'], Teams[row['teamID']][2], row['divID'] ))
	else:
		Teams[row['teamID'] ] = [row['lgID'], row['franchID'], row['divID']]


file1.close()   # <---IMPORTANT