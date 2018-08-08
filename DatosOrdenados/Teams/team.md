# Teams
## Información relativo a los equipos

- Tabla Team Original hace referencia a estadistica de los equipos por año, la podríamos dividir en una tabla que contenga información netamente del equipo como nombre, franquicia, etc y otra con la estadistica de cada temporada!

- Idea separa en Season - Teams - HomeGames(No necesariamente) - Parks(Extra)

------------------------------------------------------------------------------
### Tabla Original
### 2.8  Teams table

|indice| atributo | info
|------|----------|------
| 0  | yearID         | Year
| 1  | lgID           | League
| 2  | teamID         | Team
| 3  | franchID       | Franchise (links to TeamsFranchise table)
| 4  | divID          | Team's division
| 5  | Rank           | Position in final standings
| 6  | G              | Games played
| 7  | GHome          | Games played at home
| 8  | W              | Wins
| 9  | L              | Losses
| 10 | DivWin         | Division Winner (Y or N)
| 11 | WCWin          | Wild Card Winner (Y or N)
| 12 | LgWin          | League Champion(Y or N)
| 13 | WSWin          | World Series Winner (Y or N)
| 14 | R              | Runs scored
| 15 | AB             | At bats
| 16 | H              | Hits by batters
| 17 | 2B             | Doubles
| 18 | 3B             | Triples
| 19 | HR             | Homeruns by batters
| 20 | BB             | Walks by batters
| 21 | SO             | Strikeouts by batters
| 22 | SB             | Stolen bases
| 23 | CS             | Caught stealing
| 24 | HBP            | Batters hit by pitch
| 25 | SF             | Sacrifice flies
| 26 | RA             | Opponents runs scored
| 27 | ER             | Earned runs allowed
| 28 | ERA            | Earned run average
| 29 | CG             | Complete games
| 30 | SHO            | Shutouts
| 31 | SV             | Saves
| 32 | IPOuts         | Outs Pitched (innings pitched x 3)
| 33 | HA             | Hits allowed
| 34 | HRA            | Homeruns allowed
| 35 | BBA            | Walks allowed
| 36 | SOA            | Strikeouts by pitchers
| 37 | E              | Errors
| 38 | DP             | Double Plays
| 39 | FP             | Fielding  percentage
| 40 | name           | Team's full name
| 41 | park           | Name of team's home ballpark
| 42 | attendance     | Home attendance total
| 43 | BPF            | Three-year park factor for batters
| 44 | PPF            | Three-year park factor for pitchers
| 45 | teamIDBR       | Team ID used by Baseball Reference website
| 46 | teamIDlahman45 | Team ID used in Lahman database version 4.5
| 47 | teamIDretro    | Team ID used by Retrosheet


------------------------------------------------------------------------------

2.11 TeamFranchises table

|indice| atributo | info
|------|----------|------
| 0 | franchID   | Franchise ID
| 1 | franchName | Franchise name
| 2 | active     | Whetehr team is currently active (Y or N)
| 3 | NAassoc    | ID of National Association team franchise played as

------------------------------------------------------------------------------

Parks y HomeGames

|indice| atributo | info
|------|----------|------
