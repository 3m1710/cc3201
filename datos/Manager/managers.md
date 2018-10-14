# Información sobre managers del equipo ( D.T. )

## Info
- Un D.T puede ser cambiado a mitad de temporada (+de una vez)

1. Manager Table
	
	{managerID, yearID, teamID }

	{teamID } -> {leagueID}


------------------------------------------------------------------------------
## Tablas

### 2.7  Managers table

|indice| atributo | info
|------|----------|------ 
| 1 | playerID   |    Player ID Number
| 2 | yearID     |    Year
| 3 | teamID     |    Team
| 4 | lgID       |    League
| 5 | inseason   |    Managerial order.  Zero if the individual managed the team the entire year.  Otherwise denotes where the manager appeared in the managerial order (1 for first manager, 2 for second, etc.)
| 6 | G         |     Games managed
| 7 | W         |     Wins
| 8 | L         |     Losses
| 9 | rank      |     Team's final position in standings that year
| 10| plyrMgr   |     Player Manager (denoted by 'Y')

------------------------------------------------------------------------------
------------------------------------------------------------------------------



- Creo que deberíamos desechar ManagerHalf 

### 2.13 ManagersHalf table

|indice| atributo | info
|------|----------|------
|0| playerID   | Manager ID code
|1| yearID     | Year
|2| teamID     | Team
|3| lgID       | League
|4| inseason   | Managerial order.  One if the individual managed the team the entire year.  Otherwise denotes where the manager appearedin the managerial order (1 for first manager, 2 for second, etc.)
|5| half  | First or second half of season
|6| G     | Games managed
|7| W     | Wins
|8| L     | Losses
|9| rank  | Team's position in standings for the half

------------------------------------------------------------------------------