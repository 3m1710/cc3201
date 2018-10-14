#People table: 

Contiene información de personas, tanto jugadores como managers.


Construida desde Masters:

- Se descartaron: 
	- nameFirst: Información ya se encontraba en nameGiven
	- 2 codigo finales

- Se mergearon: 
	- birthDate: se mezcla birthyear + birthmonth + birthday
	- deathDate: igual con death

- Por decidir: 
	- Se podría eliminar birthState, birthCity, deathState y deathCity

- pound -> kg
- inches -> cm

------------------------------------------------------------------------------
People csv

|indice| atributo | info
|------|----------|------

| 0  personID     |  A unique code asssigned to each player.  The playerID links the data in this file with records in the other files.  apellido + 2 primeras letras de nombre + numero
| 1  | givenName     |  Player's given name (typically first and middle)
| 2  | lastName      |  Player's last name
| 3  | birthDate     |  Date player was born
| 4  | birthCountry  |  Country where player was born
| 5  | birthState    |  State where player was born
| 6  | birthCity     |  City where player was born
| 7  | deathDate     |  Date player died
| 8  | deathCountry  |  Country where player died
| 9  | deathState    |  State where player died
| 10 | deathCity     |  City where player died
| 11 | weight        |  Player's weight in pounds
| 12 | height        |  Player's height in inches
| 13 | bats          |  Player's batting hand (left, right, or both)         
| 14 | throws        |  Player's throwing hand (left or right)
| 15 | debut         |  Date that player made first major league appearance
| 16 | finalGame     |  Date that player made first major league appearance (blank if still active)

------------------------------------------------------------------------------

Original People

2.1 MASTER table

|indice| atributo | info
|------|----------|------
| 0  | playerID      | A unique code asssigned to each player.  The playerID links the data in this file with records in the other files.
| 1  | birthYear     | Year player was born
| 2  | birthMonth    | Month player was born
| 3  | birthDay      | Day player was born
| 4  | birthCountry  | Country where player was born
| 5  | birthState    | State where player was born
| 6  | birthCity     | City where player was born
| 7  | deathYear     | Year player died
| 8  | deathMonth    | Month player died
| 9  | deathDay      | Day player died
| 10 | deathCountry |  Country where player died
| 11 | deathState   |  State where player died
| 12 | deathCity    |  City where player died
| 13 | nameFirst    |  Player's first name
| 14 | nameLast     |  Player's last name
| 15 | nameGiven    |  Player's given name (typically first and middle)
| 16 | weight       |  Player's weight in pounds
| 17 | height       |  Player's height in inches
| 18 | bats         |  Player's batting hand (left, right, or both)         
| 19 | throws       |  Player's throwing hand (left or right)
| 20 | debut        |  Date that player made first major league appearance
| 21 | finalGame    |  Date that player made first major league appearance (blank if still active)
| 22 | retroID      |  ID used by retrosheet
| 23 | bbrefID      |  ID used by Baseball Reference website