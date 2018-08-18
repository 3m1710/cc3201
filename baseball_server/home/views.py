from django.shortcuts import render
from .forms import Jugador 
from django.db import connection
from collections import namedtuple
import django_tables2 as tables
from django_tables2 import RequestConfig
from django.views import View
from .tables import TablaJugador
# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')

def team(request):
    return render(request, 'home/about.html')



class jugador(View):
    #form_class = MyForm

    template_name = 'home/consultas.html'
    my_form = Jugador


    def get(self, request, *args, **kwargs):
        # form = self.my_form(request.GET)
        # # verifica que sea valido:
        # if form.is_valid():
        #     tabla = self.get_table(request, form)
        #     return render(request, self.template_name, {'player_form': form, 'resultados':tabla})

        # else:
        form = self.my_form()
        return render(request, self.template_name, {'player_form': form})

    def post(self, request, *args, **kwargs):
        form = self.my_form(request.POST)
        # verifica que sea valido:
        if form.is_valid():
            tabla = self.get_table(request, form)
            return render(request, self.template_name, {'player_form': form, 'resultados':tabla})
        else:
            form = self.my_form()
            return render(request, self.template_name, {'player_form': form})

    def get_table(self,request,form):
        nombre = form.cleaned_data['nombre']
        nombre2 = form.cleaned_data['nombre2']
        apellido = form.cleaned_data['apellido']
        print(form.cleaned_data["ordenar"])
        sql_res = consultar_jugador(apellido, nombre, nombre2)
        if sql_res:
            # claseTabla = TableFactory(sql_res[0])
            # tabla =  claseTabla(sql_res)
            tabla =  TablaJugador(sql_res)
            RequestConfig(request).configure(tabla)
        else:
            tabla = tables.Table(data = [])
        return tabla


def consultar_jugador(lastname, givenname, middlename):
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
            cursor.execute("SELECT * FROM people")            
        elif name == "":
            cursor.execute("SELECT * FROM people WHERE lastname = %s", [lastname])
        else:
            cursor.execute("SELECT * FROM people WHERE lastname = %s and givenname like %s", [lastname, name])
        
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

#table = NameTable(data)