CREATE TABLE People (
peopleID varchar (255) primary key,
given_name varchar (255),
last_name varchar (255),
birthdate date,
birth_country varchar (255),
weight float,
height float,
bats varchar (255),
throws varchar (255),
debut date,
final_game date
);

CREATE TABLE Teams(
teamid varchar (255),
team_name varchar (255),
season_debut int,
franchise_name varchar(255),

primary key(teamid, team_name)
);


CREATE TABLE Team_Season(
year int,
teamid varchar(255),
team_name varchar(255),
league varchar(255),
division varchar(255), 
games int, 
games_at_home int,
wins int,
loses int, 
div_rank int, 
park varchar(255), 
attendance int, 
BPF int, 
PP int, 
primary key (year, teamid),
foreign key(teamid, team_name) references Teams(teamid, team_name)
);

CREATE TABLE Season(
year int,
league varchar(255),
division varchar(255), 
division_winner varchar (255),
primary key(year, league, division),
foreign key(year, division_winner) references Team_Season(year, teamid)
);


CREATE TABLE postSeason(
year int,
league varchar(255),
league_winner varchar (255),
ws_winner varchar(255), 
primary key(year, league),
foreign key(year, league_winner) references Team_Season(year, teamid)
);


CREATE TABLE Player_season_Appearances (
year int,
teamID varchar (255),
playerID varchar (255),
--lgID varchar (255),
G_all int,
GS int,
G_batting int,
G_defense int,
G_p int,
G_c int,
G_1b int,
G_2b int,
G_3b int,
G_ss int,
G_lf int,
G_cf int,
G_rf int,
G_of int,
G_dh int,
G_ph int,
G_pr int,
primary key (year, teamID, playerID),
foreign key (teamID, year) references Team_Season(teamID, year),
foreign key (playerID) references People(peopleID)
);

CREATE TABLE Player_season_Batting (
playerID varchar (255),
year int,
stint int,
teamID varchar (255),
-- lgID varchar (255),
G int,
AB int,
R int,
H int,
"2B" int,
"3B" int,
HR int,
RBI int,
SB int,
CS int,
BB int,
SO int,
IBB int,
HBP int,
SH int,
SF int,
GIDP int,
primary key ( playerID, year, teamID, stint),
foreign key (teamID, year) references Team_Season(teamID, year),
foreign key (playerID) references People(peopleID)
);


CREATE TABLE Player_season_Fielding (
playerID varchar (255),
year int,
stint int,
teamID varchar (255),
-- lgID varchar (255),
POS varchar (255),
G int,
GS int,
InnOuts int,
PO int,
A int,
E int,
DP int,
PB int,
WP int,
SB int,
CS int,
ZR int,
primary key (playerID, year, teamID , stint, pos),
foreign key (teamID, year) references Team_Season(teamID, year),
foreign key (playerID) references People(peopleID)
);


CREATE TABLE Player_season_Pitching (
playerID varchar (255),
year int,
stint int,
teamID varchar (255),
-- lgID varchar (255),
W int,
L int,
G int,
GS int,
CG int,
SHO int,
SV int,
IPouts int,
H int,
ER int,
HR int,
BB int,
SO int,
BAOpp float,
ERA float,
IBB int,
WP int,
HBP int,
BK int,
BFP int,
GF int,
R int,
SH int,
SF int,
GIDP int,
primary key (year, teamID, playerID, stint),
foreign key (teamID, year) references Team_Season(teamID, year),
foreign key (playerID) references People(peopleID)
);


CREATE TABLE Manager (
playerID varchar (255),
year int,
teamID varchar (255),
-- lgID varchar (255),
inseason int,
G int,
W int,
L int,
--rank int,
--plyrMgr varchar (255),
primary key (year, teamID, playerID, inseason),
foreign key (teamID, year) references Team_Season(teamID, year),
foreign key (playerID) references People(peopleID)
);

CREATE TABLE Awards(
	personID varchar (255),
	award_name varchar (255),
	year int,
	league varchar (255),
	tie varchar (255),
	notes varchar (255),
	category varchar(255),
	primary key (award_name, year, league, personID),
	foreign key (personID) references People(peopleID)
);



CREATE TABLE AwardsVotes (
	award_name varchar (255),
	year int,
	league varchar (255),
	personid varchar (255),
	pointsWon float,
	pointsMax float,
	votesFirst float,
	category varchar(255),
primary key (award_name, year, league, personid),
foreign key (personid) references People(peopleID)

);

CREATE TABLE Salaries (
year int,
teamID varchar (255),
--league varchar (255),
playerID varchar (255),
salary int,
primary key(playerID, year, teamID),
foreign key (teamID, year) references Team_Season(teamID, year),
foreign key (playerID) references People(peopleID)

);

CREATE TABLE HallOfFame (
playerID varchar(255),
year int,
votedBy varchar(255),
ballots int,
needed int,
votes int,
inducted varchar(255),
category varchar(255),
needed_note varchar(255),
primary key (year, playerID, category, inducted, votedBy),
foreign key (playerID) references People(peopleID)
);



copy People FROM '/home/cc3201/cc3201/DatosOrdenados/People/People.csv' DELIMITER ',' CSV HEADER;
copy Teams FROM '/home/cc3201/cc3201/DatosOrdenados/Teams/Teams2.csv' DELIMITER ',' CSV HEADER;
copy team_season FROM '/home/cc3201/cc3201/DatosOrdenados/Teams/teams_season.csv' DELIMITER ',' CSV HEADER;

copy Player_season_Appearances FROM '/home/cc3201/cc3201/DatosOrdenados/Jugador/Appearances.csv' DELIMITER ',' CSV HEADER;
copy Player_season_Batting FROM '/home/cc3201/cc3201/DatosOrdenados/Jugador/Batting.csv' DELIMITER ',' CSV HEADER;
copy Player_season_Fielding FROM '/home/cc3201/cc3201/DatosOrdenados/Jugador/Fielding.csv' DELIMITER ',' CSV HEADER;
copy Player_season_Pitching FROM '/home/cc3201/cc3201/DatosOrdenados/Jugador/Pitching.csv' DELIMITER ',' CSV HEADER;
copy Manager FROM '/home/cc3201/cc3201/DatosOrdenados/Manager/Managers.csv' DELIMITER ',' CSV HEADER;
copy Salaries FROM '/home/cc3201/cc3201/DatosOrdenados/JugadorExtra/Salaries.csv' DELIMITER ',' CSV HEADER;
copy HallOfFame FROM '/home/cc3201/cc3201/DatosOrdenados/JugadorExtra/HallOfFame.csv' DELIMITER ',' CSV HEADER;
copy Awards FROM '/home/cc3201/cc3201/DatosOrdenados/JugadorExtra/Awards.csv' DELIMITER ',' CSV HEADER;
copy AwardsVotes FROM '/home/cc3201/cc3201/DatosOrdenados/JugadorExtra/AwardsVotes.csv' DELIMITER ',' CSV HEADER;

-- NOTAS de implementación
 -- Player Apparecences <- thompan01 not in player  - 53 sb as float
 -- Batting Se añade stint a llave primaria por linea 21
 -- Pitching : - hbp 468 float
 -- 		  -Se agrega stint a llave primaria por 342 
 -- Fielding: - Se agrega pos a llave primaria por 4
 -- Awards:   cruzne

