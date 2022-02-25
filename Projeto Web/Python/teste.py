
from http.client import ImproperConnectionState
import mysql.connector


def Conectar():
    return mysql.connector.connect(host="10.255.1.3", user="omb.mrm", password="5456mrm", database="Fimm_Brasil")


def Desconectar(conn):
    conn.close()

conn = Conectar()

comandos = conn.cursor()
comandos.execute("SELECT * FROM Funcionarios;")
dados = comandos.fetchall()
print(dados)
conn.commit()
Desconectar(conn)




#INSERT INTO Solicitacao(usuario,Epis,cod,Tipo,Quantidade,Tamanho,Dia)values('Mohammed','Bota','10','Calçado','2','39','25/02/2022');



