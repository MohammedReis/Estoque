from select import select
from sqlite3 import Cursor
import Conexao
import Cripto


def Select_Login():
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("SELECT * FROM login;")
    dados = comandos.fetchall()
    conn.commit()
    Conexao.Desconectar(conn)
    return dados

def Insert_Login(usuario,senha,cargo):
    senha = Cripto.Cripto(senha)
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("INSERT INTO login(login,senha,cargo)values('"+usuario+"','"+senha+"','"+cargo+"');")
    conn.commit()
    Conexao.Desconectar(conn)
    
def Editar_Login(id,usuario,senha,cargo):
    senha = Cripto.Cripto(senha)
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("UPDATE login SET usuario = '"+usuario+"',senha ='"+senha+"',cargo='"+cargo+"' WHERE (id ='"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)
    
def Delete_Login(id):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("DELETE FROM login WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)

def Select_Epi():
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("SELECT * FROM epi;")
    dados = comandos.fetchall()
    conn.commit()
    Conexao.Desconectar(conn)
    return dados
    
def Insert_Epi(Epis,cod,tipo,quantidade,tamanho,estoque_minimo):    
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("INSERT INTO Epi(Epis,cod,Tipo,Quantidade,Tamanho,Estoque_minimo)values('"+Epis+"','"+cod+"','"+tipo+"','"+quantidade+"','"+tamanho+"','"+estoque_minimo+"');")
    conn.commit()
    Conexao.Desconectar(conn)  
    
def Delete_Epi(id):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("DELETE FROM epi WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)
    
def Editar_Epi(id,Epis,cod,tipo,quantidade,tamanho,estoque_minimo):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("UPDATE Epi SET Epis = '"+Epis+"',cod ='"+cod+"',Tipo='"+tipo+"', Quantidade ='"+quantidade+"',Tamanho = '"+tamanho+"',Estoque_minimo ='"+estoque_minimo+"' WHERE (id ='"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)
    
def Select_Solicitacao():
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("SELECT * FROM Solicitacao;")
    dados = comandos.fetchall()
    conn.commit()
    Conexao.Desconectar(conn)
    return dados

def Inserir_Solicitacao(usuario,Epis,cod,Tipo,Quantidade,Tamanho,Dia):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("INSERT INTO Solicitacao(usuario,Epis,cod,Tipo,Quantidade,Tamanho,Dia)values('"+usuario+"','"+Epis+"','"+cod+"','"+Tipo+"','"+Quantidade+"','"+Tamanho+"','"+Dia+"');")
    conn.commit()
    Conexao.Desconectar(conn)  

def Editar_Solicitacao(id,usuario,Epis,cod,Tipo,Quantidade,Tamanho,Dia):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("UPDATE Solicitacao SET usuario = '"+usuario+"',Epis = '"+Epis+"',cod ='"+cod+"',Tipo='"+Tipo+"', Quantidade ='"+Quantidade+"',Tamanho = '"+Tamanho+"',Dia='"+Dia+"' WHERE (id ='"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)   
    
def Delete_Solicitacao(id):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("DELETE FROM Solicitacao WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)

def Select_Funcionarios():
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("SELECT * FROM Funcionarios;")
    dados = comandos.fetchall()
    conn.commit()
    Conexao.Desconectar(conn)
    return dados

def Insert_Funcionarios(Matricula,Nome,Cpf,Base,Data_Admissao,Data_Demissao):    
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("INSERT INTO Funcionarios (Matricula,Nome,Cpf,Base,Data_Admissao,Data_Demissao)VALUES('"+Matricula+"','"+Nome+"','"+Cpf+"','"+Base+"','"+Data_Admissao+"','"+Data_Demissao+"');")
    conn.commit()
    Conexao.Desconectar(conn)

def Editar_Funcionarios(id,Matricula,Nome,Cpf,Base,Data_Admissao,Data_Demissao):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("UPDATE Funcionarios SET Matricula = '"+Matricula+"',Nome = '"+Nome+"',Cpf ='"+Cpf+"',Base='"+Base+"', Data_Admissao ='"+Data_Admissao+"',Data_Demissao = '"+Data_Demissao+"' WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn) 
    
def Delete_Funcionarios(id):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("DELETE FROM Funcionarios WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)

def Select_Tamanho():
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("SELECT * FROM Tamanho;")
    dados = comandos.fetchall()
    conn.commit()
    Conexao.Desconectar(conn)
    return dados

def Insert_Tamanho(Matricula,Nome,Bota,Calca,Camisa,Jaqueta):    
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("INSERT INTO Tamanho (Matricula,Nome,Bota,Calca,Camisa,Jaqueta)VALUES('"+Matricula+"','"+Nome+"','"+Bota+"','"+Calca+"','"+Camisa+"','"+Jaqueta+"');")
    conn.commit()
    Conexao.Desconectar(conn)
    
def Editar_Tamanho(id,Matricula,Nome,Bota,Calca,Camisa,Jaqueta):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("UPDATE Tamanho SET Matricula = '"+Matricula+"', Nome = '"+Nome+"', bota ='"+Bota+"',Calca='"+Calca+"', Camisa ='"+Camisa+"',Jaqueta = '"+Jaqueta+"' WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn) 
    
def Delete_Tamanho(id):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("DELETE FROM Tamanho WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)
    
def Select_Fornecedor():
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("SELECT * FROM Fornecedor;")
    dados = comandos.fetchall()
    conn.commit()
    Conexao.Desconectar(conn)
    return dados

def Insert_Fornecedor(Fornecedor,CNPJ,Endereco):    
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("INSERT INTO Fornecedor (Fornecedor,CNPJ,Endereco)VALUES('"+Fornecedor+"','"+CNPJ+"','"+Endereco+"');")
    conn.commit()
    Conexao.Desconectar(conn)

def Editar_Fornecedor(id,Fornecedor,CNPJ,Endereco):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("UPDATE Fornecedor SET Fornecedor = '"+Fornecedor+"', CNPJ = '"+CNPJ+"', Endereco ='"+Endereco+"' WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)
    
def Delete_Fornecedor(id):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("DELETE FROM Fornecedor WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)

def Select_Fornecedor_Contato():
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("SELECT * FROM Fornecedor_Contato;")
    dados = comandos.fetchall()
    conn.commit()
    Conexao.Desconectar(conn)
    return dados

def Insert_Fornecedor_Contato(CNPJ,Telefone,Email):    
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("INSERT INTO Fornecedor_Contato (CNPJ,Telefone,Email)VALUES('"+CNPJ+"','"+Telefone+"','"+Email+"');")
    conn.commit()
    Conexao.Desconectar(conn)

def Editar_Fornecedor_Contato(id,CNPJ,Telefone,Email):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("UPDATE Fornecedor_Contato SET CNPJ = '"+CNPJ+"', Telefone = '"+Telefone+"', Email ='"+Email+"' WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)

def Delete_Fornecedor_Contato(id):
    conn = Conexao.Conectar()
    comandos = conn.cursor()
    comandos.execute("DELETE FROM Fornecedor_Contato WHERE (id = '"+id+"');")
    conn.commit()
    Conexao.Desconectar(conn)
