from http.client import ImproperConnectionState
import mysql.connector

def Conectar():
    return mysql.connector.connect(host="10.255.1.3", user="omb.mrm", password="5456mrm", database="Fimm_Brasil")


def Desconectar(conn):
    conn.close()
    









