import Token
import Comandos
import Cripto


def Validar_Login(Matricula,Password):
    login = Matricula
    senha = Password

    usuario = Comandos.Select_Login(login,senha)
    senha = Cripto.Cripto(senha) 
    if(usuario != []):
        if (usuario[0][1] == login and usuario[0][2] == senha):
            token = Token.criar_acess_token(login,senha)
            token = Token.Decodificar(token)
            lista = token['some']
            print(lista)
            if(lista['sub']==login and lista['name']== senha):
                print("usuario Autenticado")
            else:
                print("usuario não autenticado")
    else:
        print("Usuario ou senha incorretos")