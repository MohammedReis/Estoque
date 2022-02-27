import jwt


SECURIT_KEY = "479B985D1330457A58EEC555EB8D89D8E3C9844E543681F1B3C2E7D21CEBF2CE"
ALGORITHM = "HS256"
def criar_acess_token(Matricula,senha):
    payload = {
    "sub": Matricula,
    "name": senha,
    "exp": "30"
    }
    encoded = jwt.encode({"some": payload}, SECURIT_KEY, algorithm="HS256")
    return encoded
    
def Decodificar(encoded)   :
    descodific = jwt.decode(encoded, SECURIT_KEY, algorithms=["HS256"])
    return descodific

    