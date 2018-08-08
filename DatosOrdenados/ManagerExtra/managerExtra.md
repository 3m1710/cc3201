## Información extra de los managers que puede ser utilizada para consultas semi interesantes!

1. AwardsManager: Premios obtenidos por los jugadores
	- {player, year, award}


2. AwardsShareManager: Premios obtenidos por jugadores que sea por votación popular
	- {player, year, award}

- Consultar jugadorExtra !


------------------------------------------------------------------------------
2.17 AwardsManagers table

|indice| atributo | info
|------|----------|------
| 0 |playerID |  Manager ID code
| 1 |awardID  |  Name of award won
| 2 |yearID   |  Year
| 3 |lgID     |  League
| 4 |tie      |  Award was a tie (Y or N)
| 5 |notes    |  Notes about the award

------------------------------------------------------------------------------
------------------------------------------------------------------------------
2.19 AwardsShareManagers table

|indice| atributo | info
|------|----------|------
| 0 | awardID    | name of award votes were received for
| 1 | yearID     | Year
| 2 | lgID       | League
| 3 | playerID   | Manager ID code
| 4 | pointsWon  | Number of points received
| 5 | pointsMax  | Maximum numner of points possible
| 6 | votesFirst | Number of first place votes

------------------------------------------------------------------------------