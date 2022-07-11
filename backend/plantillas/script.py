import requests
import os
import datetime

def OpenData(estacion, anno, anno2, sitio, primero):
    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/"+anno+"-01-01T00:00:00UTC/fechafin/"+anno2+"-12-31T00:00:00UTC/estacion/"+estacion
    querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkb21pOTVAaG90bWFpbC5lcyIsImp0aSI6ImJiNzM0Mzg2LWUwYjEtNDZlMy04YTgxLTBkMTFjYWVmMjQwMyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNjM1NTEyMzk5LCJ1c2VySWQiOiJiYjczNDM4Ni1lMGIxLTQ2ZTMtOGE4MS0wZDExY2FlZjI0MDMiLCJyb2xlIjoiIn0.rjTXU1Jnu52ELvvUGDHF9FXZSewZa5B3P0RQKDDlju8"}
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    r = response.json()
    if r['estado']==200:
        print(anno)

        i = requests.get(r['datos']).text
        if primero==0:
            i = ", "+i[2:-2]
        elif primero==1:
            i = i[:-2]
        else:
            i = ", "+i[2:]
        with open('../static/opendata/'+sitio+".json", 'a', encoding='utf-8') as f:
            f.write(i)
        f.close()
        return 1;
    else:
        return 0;
def ExtraerDatos(estacion, sitio):
    if os.path.exists("../static/opendata/"+sitio+".txt"):
      os.remove("../static/opendata/"+sitio+".txt")
    x = datetime.datetime.now()
    print("Cargando "+sitio+" ...")
    i = 1999
    o = i+1
    bool=1;
    while o <= x.year:
        if o==x.year:
            print(sitio+" Finalizado.")
            OpenData(estacion,str(i),str(o),sitio,2)
        else:
            if bool==1:
                if OpenData(estacion,str(i),str(o),sitio,1)==1:
                    print("Primero")
                    bool=0;
            else:
                OpenData(estacion,str(i),str(o),sitio,0)
        i += 2;
        o += 2;

ExtraerDatos("9091R","Alava")
ExtraerDatos("8178D","Albacete")
ExtraerDatos("8025","Alicante")
ExtraerDatos("6297","Almeria")
ExtraerDatos("1212E","Asturias")
ExtraerDatos("2444","Avila")
ExtraerDatos("4452","Badajoz")
ExtraerDatos("B954","Ibiza")
ExtraerDatos("B893","Menorca")
ExtraerDatos("B278","Mallorca")
ExtraerDatos("0076","Barcelona")
ExtraerDatos("1082","Bilbao")
ExtraerDatos("2331","Burgos")
ExtraerDatos("3469A","Caceres")
ExtraerDatos("5960","Cadiz")
ExtraerDatos("1111X","Cantabria")
ExtraerDatos("9563X","Castellon")
ExtraerDatos("4121","CiudadReal")
ExtraerDatos("5402","Cordoba")
ExtraerDatos("1387","ACoruna")
ExtraerDatos("8096","Cuenca")
ExtraerDatos("0367","Girona")
ExtraerDatos("5530E","Granada")
ExtraerDatos("3168D","Guadalajara")
ExtraerDatos("1014A","Guipuzcua")
ExtraerDatos("4642E","Huelva")
ExtraerDatos("9898","Huesca")
ExtraerDatos("C929I","ElHierro")
ExtraerDatos("5270B","Jaen")
ExtraerDatos("2661","Leon")
ExtraerDatos("9990X","Lleida")
ExtraerDatos("1505","Lugo")
ExtraerDatos("6155A","Malaga")
ExtraerDatos("7031","Murcia")
ExtraerDatos("9263D","Navarra")
ExtraerDatos("1690A","Ourense")
ExtraerDatos("2401","Palencia")
ExtraerDatos("C029O","Lanzarote")
ExtraerDatos("1484C","Pontevedra")
ExtraerDatos("9170","LaRioja")
ExtraerDatos("2870","Salamanca")
ExtraerDatos("C449C","Tenerife")
ExtraerDatos("2150H","Segovia")
ExtraerDatos("5783","Sevilla")
ExtraerDatos("2030","Soria")
ExtraerDatos("0016A","Tarragona")
ExtraerDatos("8368U","Teruel")
ExtraerDatos("3365A","Toledo")
ExtraerDatos("8416Y","Valencia")
ExtraerDatos("2422","Valladolid")
ExtraerDatos("2614","Zamora")
ExtraerDatos("9576C","Zaragoza")
ExtraerDatos("3195","Madrid")
ExtraerDatos("6000A","Melilla")
ExtraerDatos("5000C","Ceuta")
