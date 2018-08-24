from django.shortcuts import render
from django.db import connection
from collections import namedtuple
import django_tables2 as tables
from django_tables2 import RequestConfig
from django.views import View

from .tables import *
import home.forms as forms

# from .forms import Jugador 
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def team(request):
    return render(request, 'home/about.html')

def consultas(request, query_id):
    dic = {'1':consulta1, '2':consulta2, '3': consulta3, '4':consulta4, '5':consulta5}
    if query_id in dic:
        return dic[query_id].as_view()(request)
    else:
        return index(request)


class ConsultaGeneral(View):
    def get(self, request,  *args, **kwargs):
        form = self.my_form(request.GET)
        # verifica que sea valido:
        if form.is_valid():
            tabla = self.get_table(request, form)
            return render(request, self.template_name, {'message': self.msg, 'form': form, 'resultados':tabla})
        else:

            form = self.my_form()
        return render(request, self.template_name, {'message': self.msg , 'form': form})

    def post(self, request,query_id=1, *args, **kwargs):
        
        form = self.my_form(request.POST)

        if form.is_valid():
            tabla = self.get_table(request, form)
            return render(request, self.template_name, {'message': self.msg,'form': form, 'resultados':tabla})
        else:
            form = self.my_form()
            return render(request, self.template_name, {'message': self.msg,'form': form})

    def get_table(self, request, form):

        sql_res = self.consultar(form)
        if sql_res:
            tabla = self.my_table(sql_res)
            RequestConfig(request).configure(tabla)
            return tabla
        else:
            tabla = self.my_table([])
            return tabla



class manager(ConsultaGeneral):

    template_name = 'home/consultas.html'
    my_form = forms.Jugador
    my_table = TablaManager
    msg = "<h2> Busca entre los Managers! </h2>"

    def consultar(self, form):

        givenname = form.cleaned_data['nombre']
        middlename = form.cleaned_data['nombre2']
        lastname = form.cleaned_data['apellido']

        if givenname == "":
            if middlename == "":
                name  =  ""        
            else:
                name = "% "+middlename+"%"
        else:
            if middlename == "":
                name = givenname+"%"
            else: 
                name = givenname + " " + middlename + "%"

        # lastname = "%" + lastname + "%"

        with connection.cursor() as cursor:
            
            if lastname=="" and name=="":
                print("HERE")
                cursor.execute("prepare consulta_manager as " + """SELECT  P.peopleid, P.last_name, P.given_name, P.birthdate, P.birth_country, P.debut,  min(M.year) as man_debut
                                  FROM baseball.people P, baseball.manager M 
                                  WHERE M.playerid = P.peopleid  
                                  group by P.peopleid 
                                  ORDER BY last_name desc""")

                cursor.execute("execute consulta_manager ")

            elif name == "":
                lastname = "%" + lastname + "%"

                cursor.execute("prepare consulta_manager (text) as " + """SELECT  P.peopleid, P.last_name, P.given_name, P.birthdate, P.birth_country, P.debut,  min(M.year) as man_debut
                                  FROM baseball.people P, baseball.manager M 
                                  WHERE M.playerid = P.peopleid  
                                  AND last_name like $1
                                  group by P.peopleid 
                                  ORDER BY last_name desc""", [lastname])

                cursor.execute("execute consulta_manager (%s) ",[lastname])

            else:
                lastname = "%" + lastname + "%"

                cursor.execute("prepare consulta_manager (text, text) as " + """SELECT  P.peopleid, P.last_name, P.given_name, P.birthdate, P.birth_country, P.debut,  min(M.year) as man_debut
                                  FROM baseball.people P, baseball.manager M 
                                  WHERE  M.playerid = P.peopleid
                                  AND P.last_name like $1
                                  AND P.given_name like $2
                                  group by P.peopleid
                                  ORDER BY last_name desc
                                  """, [lastname, name])
                cursor.execute("execute consulta_manager (%s, %s) ",[lastname,name])
            results = dictfetchall(cursor)
        return results

class jugador(ConsultaGeneral):
    #form_class = MyForm
    template_name = 'home/consultas.html'
    my_form = forms.Jugador
    my_table = TablaJugador
    msg = "<h2> Consulta por Jugadores </h2>"

    def consultar(self,form):
        givenname = form.cleaned_data['nombre']
        middlename = form.cleaned_data['nombre2']
        lastname = form.cleaned_data['apellido']


        if givenname == "":
            if middlename == "":
                name  =  ""        
            else:
                name = "% "+middlename+"%"
        else:
            if middlename == "":
                name = givenname+"%"
            else: 
                name = givenname + " " + middlename + "%"

        with connection.cursor() as cursor:
            
            if lastname=="":
                if name!="":
                    cursor.execute("prepare consulta_jugador (text) as " + "SELECT * FROM baseball.people WHERE given_name like $1")
                    cursor.execute("execute consulta_jugador (%s) ",[name])
                else:
                    cursor.execute("prepare consulta_jugador as " + "SELECT * FROM baseball.people")            
                    cursor.execute("execute consulta_jugador ")

            elif name == "":
                cursor.execute("prepare consulta_jugador (text) as " + "SELECT * FROM baseball.people WHERE last_name = $1")
                cursor.execute("execute consulta_jugador (%s) ",[lastname])

            else:
                cursor.execute("prepare consulta_jugador (text,text) as " + "SELECT * FROM baseball.people WHERE last_name = $1 and given_name like $2")
                cursor.execute("execute consulta_jugador (%s, %s) ",[lastname, name])
            
            results = dictfetchall(cursor)
        return results

class teams(ConsultaGeneral):
    #form_class = MyForm
    template_name = 'home/consultas.html'
    my_form = forms.Teams
    my_table = Teams
    msg = "<h2> Consulta por Equipos </h2>"

    def consultar(self,form):
        equipo = form.cleaned_data['teamid']
        nombre = form.cleaned_data['team_name']

        with connection.cursor() as cursor:
            
            if equipo:
                equipo = "%" + equipo+ "%"
                cursor.execute("prepare consulta_teams (text) as " + """
                                SELECT  T.teamid, T.team_name, T.franchise_name, T.season_debut, max(year) as last_season FROM baseball.teams T, baseball.team_season S
                                where S.teamid = T.teamid
                                AND T.teamid like $1
                                GROUP BY ( T.teamid, T.team_name, T.season_debut)
                                """)
                
                cursor.execute("execute consulta_teams (%s) ",[equipo])

            elif nombre:
                nombre = "%" + nombre+ "%"
                cursor.execute("prepare consulta_teams (text) as "+ """
                                SELECT  T.teamid, T.team_name, T.franchise_name, T.season_debut, max(year) as last_season FROM baseball.teams T, baseball.team_season S
                                where S.teamid = T.teamid
                                AND T.team_name like $1
                                GROUP BY ( T.teamid, T.team_name, T.season_debut)
                                """, [nombre])
                cursor.execute("execute consulta_teams (%s) ",[nombre])

            else:
                cursor.execute("prepare consulta_teams as "+ 
                                """SELECT  T.teamid, T.team_name, T.franchise_name, T.season_debut, max(year) as last_season FROM baseball.teams T, baseball.team_season S
                                where S.teamid = T.teamid
                                GROUP BY ( T.teamid, T.team_name, T.season_debut)""")
                cursor.execute("execute consulta_teams ")

            results = dictfetchall(cursor)
        return results


class consulta1(ConsultaGeneral):
    template_name = 'home/consultas.html'
    my_form = forms.consulta1
    my_table = Tabla1
    msg  = "<h3> ¿Quieres conocer a los compañeros de... ? </h3>"

    def consultar(self, form):
        nombre = form.cleaned_data["nombre"]
        apellido = form.cleaned_data["apellido"]
        with connection.cursor() as cursor:
            
            cursor.execute( "prepare consulta1 (text,text) as " +
            """
            SELECT  A1.playerid, P.given_name, P.last_name, A1.teamid, T.team_name, min(A1.year) as primera_temporada, max(A1.year) as ultima_temporada
            from baseball.player_season_appearances A1, baseball.teams T, baseball.people P
            
            where A1.teamid = T.teamid
            and T.team_name  = (
                select team_name from teams T2 where T2.season_debut < A1.year and T2.teamid = A1.teamid order by T2.season_debut desc limit 1
            )
            
            and P.peopleid = A1.playerid
            
            and P.given_name <> $1
            and P.last_name <> $2
            
            and ROW(A1.teamid, A1.year) in
                (select distinct A.teamid, A.year
                    from baseball.people P, baseball.player_season_appearances A 
                    where P.last_name = $2
                    and P.given_name = $1
                    and P.peopleid=A.playerid 
                )
            
            group by (A1.playerid,A1.teamid,T.team_name, P.given_name, P.last_name)
            order by A1.playerid;
            """)

            cursor.execute("execute consulta1 (%s,%s)",[nombre,apellido])

            results = dictfetchall(cursor)
            print(results)

        return results

class consulta2(ConsultaGeneral):
    template_name = 'home/consultas.html'
    my_form = forms.consulta2
    my_table = Tabla2
    msg = ' <h3> Sapear Sueldos!  </h3>'

    def consultar(self, form):
        team = form.cleaned_data["equipo"]
        with connection.cursor() as cursor:
            cursor.execute( "prepare consulta2 (text) as " + """    
                SELECT team_name, A.year, P.given_name, P.last_name, A.max as salary from (
                select distinct L.year, max(salary), T.team_name as team_name
                from salaries S, teams T, player_season_appearances A, league_winners L 
                where T.team_name =$1
                and T.teamid=L.teamid
                and A.year=L.year 
                and S.teamid=A.teamid
                and S.year=A.year
                group by L.year, T.team_name) A, salaries S, People P
                where A.year = S.year
                and A.max = S.salary
                and P.peopleid = S.playerid
                order by A.year desc;
                 """)
            cursor.execute("execute consulta2 (%s)",[team])

            results = dictfetchall(cursor)
        return results


class consulta3(ConsultaGeneral):
    msg = ' <h3> Que año fue mejor bateando... ?   </h3>'
    template_name = 'home/consultas.html'
    my_form = forms.consulta1
    my_table = Tabla3
    def consultar(self, form):
        apellido =  form.cleaned_data["apellido"]
        nombre = form.cleaned_data["nombre"]
        with connection.cursor() as cursor:
            
            cursor.execute("prepare consulta3 (text,text) as " + """    
                
                SELECT B.year, round(max(1.0*B.h / B.ab),3) as desempeno, T.team_name
                from player_season_batting B, people P, teams T
                where P.peopleid=B.playerid
                and P.given_name=$1
                and P.last_name=$2
                and B.teamid = T.teamid
                group by B.year, T.team_name
                order by desempeno desc
                limit 1
            """)
            cursor.execute("execute consulta3 (%s,%s)",[nombre,apellido])
            results = dictfetchall(cursor)
        return results

class consulta4(ConsultaGeneral):
    msg = ' <h3> Desempeño de Equipos por año   </h3>'
    template_name = 'home/consultas.html'
    my_form = forms.consulta2
    my_table = Tabla4

    def consultar(self, form):


        with connection.cursor() as cursor:
            
            team = form.cleaned_data["equipo"]

            cursor.execute("prepare consulta4  as " + """    

                SELECT A.year, A.dpp as d_players, B.dpt as d_team from (
                
                select T.year, T.team_name, round(sum(desempenho)/ count(desempenho),2) as dpp from team_season T, 
                (select playerid, year, teamid, round((h*1.0 / ab),2) as desempenho from player_season_batting
                where ab > 0) P
                where P.teamid=T.teamid
                and P.year=T.year
                group by T.team_name, T.year
                order by T.team_name, T.year) A, 
                (select T.year, T.team_name, round((T.wins*1.0 / T.games),2) as dpt from team_season T
                order by T.team_name, T.year) B
                where A.year = B.year
                and A.team_name = B.team_name
                and A.team_name = $1;
    
            """)
            cursor.execute("execute consulta4 (%s)",[team])
            results = dictfetchall(cursor)
        return results

class consulta5(ConsultaGeneral):
    msg = ' <h3> Jugadores Zurdos por Liga </h3>'
    template_name = 'home/consultas.html'
    my_form = forms.consulta5
    my_table = Tabla5

    def consultar(self, form):


        with connection.cursor() as cursor:
            liga = form.cleaned_data["league"]  
            cursor.execute("prepare consulta5  as " + """    
                SELECT L.team_name, L.zurdos, R.diestros
                from

                (select T.team_name, count(P.bats) as zurdos
                from teams T, people P, postseason S, player_season_appearances A
                where P.bats = 'L'
                and P.peopleid= A.playerid
                and A.teamid=T.teamid
                and S.league_winner=T.teamid
                and S.league = $1
                group by T.team_name) as L

                inner join

                (select T.team_name, count(P.bats) as diestros
                from teams T, people P, postseason S, player_season_appearances A
                where P.bats = 'R'
                and P.peopleid= A.playerid
                and A.teamid=T.teamid
                and S.league_winner=T.teamid
                and S.league = $1
                group by T.team_name) as R

                on L.team_name = R.team_name
                order by l.zurdos desc;
            """)
            cursor.execute("execute consulta5 (%s)",[liga])
            results = dictfetchall(cursor)
        return results
        


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]