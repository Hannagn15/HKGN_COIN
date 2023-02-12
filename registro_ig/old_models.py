import sqlite3
from config import *



def select_all():
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()

    res = cur.execute("select id,date,concept,quantity from movements order by date;")

    filas = res.fetchall()#capturo las filas de datos
    columnas= res.description#capturo los nombres de columnas

    #objetivo crear una lista de diccionario con filas y columnas

    
    resultado =[]#lista para guadar diccionario
   
    for fila in filas:
        dato={}#diccionario para cada registro
        posicion=0#posicion de columna

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)

    con.close()

    return resultado


def insert(registro):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()

    cur.execute("insert into movements(date,concept,quantity) values(?,?,?)",registro)

    con.commit()#funcion que registra finalmente

    con.close()
   


def select_by(id):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()

    res = cur.execute(f"select id,date,concept,quantity from movements where id={id}")

    resultado = res.fetchall()

    con.close()

    return resultado[0]

def delete_by(id):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()

    cur.execute(f"delete from movements where id={id}")

    con.commit()

    con.close()

