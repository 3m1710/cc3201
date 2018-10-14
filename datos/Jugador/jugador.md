#Estadisticas sobre los jugadores de baseball

## Contiene las siguiente tablas

1. Appareances: Información de las posiciones en que jugó un jugador para determinado equipo en determinada temporada. 
2. Batting Table: Información de bateo de jugadores para determinado equipo en determinada temporada. 
3. Pitching table: Información de pitching de jugadores para determinado equipo en determinada temporada. 
4. Fielding Table: Información de Fielding para determinado equipo en determinada temporada. 

## Ideas: 

- Se podrían Mezclar las 4 tablas en 1 :s
- Todas tienen la siguiente llave candidata: 
	{jugador, team, año}
- Puede que exista la siguiente dependencia funcional: 
	{team} -> {liga}
- Ni idea que significa stint,  pero parece que indica cuando un jugador cambia de equipo ( Si jugó en 2 equipos en una misma temporada,permite indicar en que equipo jugó primero)
------------------------------------------------------------------------------
------------------------------------------------------------------------------

## Tablas


### 2.2 Batting Table

|indice| atributo| info
|----|-----------|----------
| 0  | playerID  | Player ID code
| 1  | yearID    | Year
| 2  | stint     | player's stint (order of appearances within a season)
| 3  | teamID    | Team
| 4  | lgID      | League
| 5  | G         | Games
| 6  | AB        | At Bats
| 7  | R         | Runs
| 8  | H         | Hits
| 9  | 2B        | Doubles
| 10 | 3B        | Triples
| 11 | HR        | Homeruns
| 12 | RBI       | Runs Batted In
| 13 | SB        | Stolen Bases
| 14 | CS        | Caught Stealing
| 15 | BB        | Base on Balls
| 16 | SO        | Strikeouts
| 17 | IBB       | Intentional walks
| 18 | HBP       | Hit by pitch
| 19 | SH        | Sacrifice hits
| 20 | SF        | Sacrifice flies
| 21 | GIDP      | Grounded into double plays


### 2.3 Pitching table

|indice| atributo| info
|----|-----------|----------
| 0  | playerID | Player ID code
| 1  | yearID   | Year
| 2  | stint    | player's stint (order of appearances within a season)
| 3  | teamID   | Team
| 4  | lgID     | League
| 5  | W        | Wins
| 6  | L        | Losses
| 7  | G        | Games
| 8  | GS       | Games Started
| 9  | CG       | Complete Games 
| 10 | SHO      | Shutouts
| 11 | SV       | Saves
| 12 | IPOuts   | Outs Pitched (innings pitched x 3)
| 13 | H        | Hits
| 14 | ER       | Earned Runs
| 15 | HR       | Homeruns
| 16 | BB       | Walks
| 17 | SO       | Strikeouts
| 18 | BAOpp    | Opponent's Batting Average
| 19 | ERA      | Earned Run Average
| 20 | IBB      | Intentional Walks
| 21 | WP       | Wild Pitches
| 22 | HBP      | Batters Hit By Pitch
| 23 | BK       | Balks
| 24 | BFP      | Batters faced by Pitcher
| 25 | GF       | Games Finished
| 26 | R        | Runs Allowed
| 27 | SH       | Sacrifices by opposing batters
| 28 | SF       | Sacrifice flies by opposing batters
| 29 | GIDP     | Grounded into double plays by opposing batter

### 2.4 Fielding Table

|indice| atributo| info
|----|-----------|----------
| 0  | playerID | Player ID code
| 1  | yearID   | Year
| 2  | stint    | player's stint (order of appearances within a season)
| 3  | teamID   | Team
| 4  | lgID     | League
| 5  | Pos      | Position
| 6  | G        | Games 
| 7  | GS       | Games Started
| 8  | InnOuts  | Time played in the field expressed as outs 
| 9  | PO       | Putouts
| 10 | A        | Assists
| 11 | E        | Errors
| 12 | DP       | Double Plays
| 13 | PB       | Passed Balls (by catchers)
| 14 | WP       | Wild Pitches (by catchers)
| 15 | SB       | Opponent Stolen Bases (by catchers)
| 16 | CS       | Opponents Caught Stealing (by catchers)
| 17 | ZR       | Zone Rating

### 2.22 Appearances table

|indice| atributo| info
|----|-----------|----------
| 0  | yearID    | Year
| 1  | teamID    | Team
| 2  | lgID      | League
| 3  | playerID  | Player ID code
| 4  | G_all     | Total games played
| 5  | GS        | Games started
| 6  | G_batting | Games in which player batted
| 7  | G_defense | Games in which player appeared on defense
| 8  | G_p       | Games as pitcher
| 9  | G_c       | Games as catcher
| 10 | G_1b      | Games as firstbaseman
| 11 | G_2b      | Games as secondbaseman
| 12 | G_3b      | Games as thirdbaseman
| 13 | G_ss      | Games as shortstop
| 14 | G_lf      | Games as leftfielder
| 15 | G_cf      | Games as centerfielder
| 16 | G_rf      | Games as right fielder
| 17 | G_of      | Games as outfielder
| 18 | G_dh      | Games as designated hitter
| 19 | G_ph      | Games as pinch hitter
| 20 | G_pr      | Games as pinch runner

------------------------------------------------------------------------------