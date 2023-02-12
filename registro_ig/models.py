import sqlite3
from config import *
from registro_ig.conexion import Conexion
import requests 
apiKey = '356A76DB-5D23-4441-A990-79B713A11932'

def select_all():
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()

    res= cur.execute("select id,date,moneda_from,cantidad_from,moneda_to,cantidad_to from movements order by date;")

    filas = res.fetchall()
    columnas= res.description

 
    resultado =[]#lista para guardar dic  
    dato={}#dic registro 
    posicion=0
    for fila in filas:
        dato={}
        posicion=0

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)


    return resultado 

def insert(registro):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()

    cur.execute("insert into movements(date,hora,moneda_from,cantidad_from,moneda_to,cantidad_to) values(?,?,?,?,?,?');",registro)
    
    con.commit()



def select_ingreso():
    connectSelectIngreso=Conexion("SELECT sum(quantity) FROM movements WHERE quantity>0")
    resultado = connectSelectIngreso.res.fetchall()
    connectSelectIngreso.con.close()
    return resultado[0][0]


def select_egreso():  
    connectSelectEgreso=Conexion("SELECT sum(CANTIDAD_FROM) FROM movements WHERE CANTIDAD_FROM<0")
    resultado = connectSelectEgreso.res.fetchall()
    connectSelectEgreso.con.close()
    return resultado[0][0]


def select_all():
    connect = Conexion("select id,date,moneda_from,cantidad_from,moneda_to,cantidad_to from movements order by date;")
    filas = connect.res.fetchall()#capturo las filas de datos
    columnas= connect.res.description#capturo los nombres de columnas

    #objetivo crear una lista de diccionario con filas y columnas

    resultado =[]#lista para guadar diccionario
   
    for fila in filas:
        dato={}#diccionario para cada registro
        posicion=0#posicion de columna

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()

    return resultado


def insert(registro):
    connectInsert = Conexion("insert into movements(date,hora,moneda_from,cantidad_from,moneda_to,cantidad_to) values(?,?,?,?,?,?');",registro)
    connectInsert.con.commit()#funcion que registra finalmente
    connectInsert.con.close()
   

def update_by(id,registro):#['date','concept','quantity']
    connectUpdate=Conexion(f"UPDATE movements SET date=?,concept=?,quantity=? WHERE id={id}",registro)
    connectUpdate.con.commit()
    connectUpdate.con.close()

def get_transaction():

    euros = float('1000')
    if euros is None:
        return "Por favor proporcione una cantidad en euros a convertir"
    # Realizar la petición a la API CoinAPI para obtener el precio actual de BTC
    response = requests.get(f'https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey={apiKey}')
    if response.status_code != 200:
        return "No se pudo obtener el precio actual de BTC"
    # Calcular la cantidad de BTC equivalente a la cantidad de euros proporcionada
    btc_price = response.json()["rate"]
    btc_amount = float(euros) / btc_price
    return print(f"{euros} EUR son {btc_amount} BTC")

'''euros = float('20000')

response = requests.get(f'https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey={apiKey}')

btc_price = response.json()["rate"]
btc_amount = float(euros) / btc_price


print(euros)
print(response)
print(btc_price)
print(btc_amount)

'''
get_transaction()