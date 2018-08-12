#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


file1 = open('../../DatosOriginales/Teams.csv', 'rb')

original_fields = ['yearID','lgID','teamID','franchID','divID','Rank','G','GHome','W','L','DivWin','WCWin','LgWin','WSWin','R','AB','H','2B','3B','HR','BB','SO','SB','CS','HBP','SF','RA','ER','ERA','CG','SHO','SV','IPOuts','HA','HRA','BBA','SOA','E','DP','FP','name','park','attendance','BPF','PPF']
reader = csv.DictReader(file1, delimiter=',', fieldnames=original_fields)


file2 = open('Teams.csv', 'wb')
fieldnames = ["yearID","lgID","divID","teamID","name","franchID","Rank","G","GHome","W","L","DivWin","WCWin","LgWin","WSWin","R","AB","H","2B","3B","HR","BB","SO","SB","CS","HBP","SF","RA","ER","ERA","CG","SHO","SV","IPOuts","HA","HRA","BBA","SOA","E","DP","FP","park","attendance","BPF","PPF"]
writer = csv.DictWriter(file2, delimiter=',', fieldnames=fieldnames)
writer.writeheader()  

next(reader)



Teams = {}
next(reader)
for row in reader:		
	new_row = {}
	new_row["yearID"]	 = row["yearID"]
	new_row["teamID"]	 = row["teamID"]
	new_row["lgID"]		 = row["lgID"]
	new_row["divID"]	 = row["divID"]
	new_row["name"]		 = row["name"]
	new_row["franchID"]	 = row["franchID"]
	new_row["Rank"]		 = row["Rank"]
	new_row["G"]		 = row["G"]
	new_row["GHome"]	 = row["GHome"]
	new_row["W"]		 = row["W"]
	new_row["L"]		 = row["L"]
	new_row["DivWin"]	 = row["DivWin"]
	new_row["WCWin"]	 = row["WCWin"]
	new_row["LgWin"]	 = row["LgWin"]
	new_row["WSWin"]	 = row["WSWin"]
	new_row["R"]		 = row["R"]
	new_row["AB"]		 = row["AB"]
	new_row["H"]		 = row["H"]
	new_row["2B"]		 = row["2B"]
	new_row["3B"]		 = row["3B"]
	new_row["HR"]		 = row["HR"]
	new_row["BB"]		 = row["BB"]
	new_row["SO"]		 = row["SO"]
	new_row["SB"]		 = row["SB"]
	new_row["CS"]		 = row["CS"]
	new_row["HBP"]		 = row["HBP"]
	new_row["SF"]		 = row["SF"]
	new_row["RA"]		 = row["RA"]
	new_row["ER"]		 = row["ER"]
	new_row["ERA"]		 = row["ERA"]
	new_row["CG"]		 = row["CG"]
	new_row["SHO"]		 = row["SHO"]
	new_row["SV"]		 = row["SV"]
	new_row["IPOuts"]	 = row["IPOuts"]
	new_row["HA"]		 = row["HA"]
	new_row["HRA"]		 = row["HRA"]
	new_row["BBA"]		 = row["BBA"]
	new_row["SOA"]		 = row["SOA"]
	new_row["E"]		 = row["E"]
	new_row["DP"]		 = row["DP"]
	new_row["FP"]		 = row["FP"]
	new_row["park"]		 = row["park"]
	new_row["attendance"] = row["attendance"]
	new_row["BPF"]		 = row["BPF"]
	new_row["PPF"]		 = row["PPF"]

	writer.writerow(new_row)

file1.close() 
file2.close()