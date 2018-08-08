# Jugador Extra
## Información extra de los jugadores que puede ser utilizada para consultas semi interesantes!

1. Salaries : Sueldos de Jugadores en determinado equipo y año. 
	- {player, year, team}

2. AwardsPlayers: Premios obtenidos por los jugadores
	- {player, year, award}


3. AwardsSharePlayer: Premios obtenidos por jugadores que sea por votación popular
	
	- Ideas: 
		- De alguna manera mezclar Awards Players y AwardsSharePlayers
		- De alguna manera mezclar AwardsPlayers y AwardsManagers

	- {player, year, award}

4. HallofFame: Votaciones de Salon de la Fama para jugadores y managers
	- {player, year} (un jugador puede aparecer más de una vez) 
		- investigar si un jugador puede aparecer más de una vez en un mismo año

5. AllStar : Apariciones de jugadores en partidos de estrellas. 
	- {player, year}

6.  Extra Extra: College - Schools: 
	- Información de Jugadores que jugaron en sus universidades


------------------------------------------------------------------------------
------------------------------------------------------------------------------
## Tablas

### 2.15 Salaries table

|indice| atributo | info
|------|----------|------
| 0  | yearID     | Year
| 1  | teamID     | Team
| 2  | lgID       | League
| 3  | playerID   | Player ID code
| 4  | salary     | Salary

### 2.18 AwardsPlayers table

|indice| atributo | info
|------|----------|------
| 0  | playerID   | Player ID code
| 1  | awardID    | Name of award won
| 2  | yearID     | Year
| 3  | lgID       | League
| 4  | tie        | Award was a tie (Y or N)
| 5  | notes      | Notes about the award


### 2.20 AwardsSharePlayers table

|indice| atributo | info
|------|----------|------
|	1   |awardID     |   name of award votes were received for
|	2   |yearID      |   Year
|	3   |lgID        |   League
|	4   |playerID    |   Player ID code
|	5   |pointsWon   |   Number of points received
|	6   |pointsMax   |   Maximum numner of points possible
|	7   |votesFirst  |   Number of first place votes

### 2.6  HallOfFame table

|indice| atributo | info
|------|----------|------
| 1 |  playerID    | Player ID code
| 2 |  yearID      | Year of ballot
| 3 |  votedBy     | Method by which player was voted upon
| 4 |  ballots     | Total ballots cast in that year
| 5 |  needed      | Number of votes needed for selection in that year
| 6 |  votes       | Total votes received
| 7 |  inducted    | Whether player was inducted by that vote or not (Y or N)
| 8 |  category    | Category in which candidate was honored
| 9 |  needed_note | Explanation of qualifiers for special elections

### 2.5  AllstarFull table

|indice| atributo | info
|------|----------|------
| 1 | playerID     | Player ID code
| 2 | YearID       | Year
| 3 | gameNum      | Game number (zero if only one All-Star game played that season)
| 4 | gameID       | Retrosheet ID for the game idea
| 5 | teamID       | Team
| 6 | lgID         | League
| 7 | GP           | 1 if Played in the game
| 8 | startingPos  | If player was game starter, the position played

------------------------------------------------------------------------------
------------------------------------------------------------------------------

###2.23 Schools table

|indice| atributo | info
|------|----------|------
| 1 | schoolID    |   school ID code
| 2 | schoolName  |   school name
| 3 | schoolCity  |   city where school is located
| 4 | schoolState |   state where school's city is located
| 5 | schoolNick  |   nickname for school's baseball team


### 2.24 CollegePlaying table

|indice| atributo | info
|------|----------|------
| 1 |playerid | Player ID code
| 2 |schoolID | school ID code
| 3 |year     | year
------------------------------------------------------------------------------