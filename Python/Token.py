from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = '479B985D1330457A58EEC555EB8D89D8E3C9844E543681F1B3C2E7D21CEBF2CE'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 30

def criar_acess_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    dados.update({'exp': expiracao})
    token_jwt = jwt.encode(dados, SECRET_KEY,algorithm=ALGORITHM)
    return  token_jwt

def FunctionName(token : str):
    carga = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
    return carga.get('sub')
    