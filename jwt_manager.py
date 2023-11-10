from jwt import encode,decode

def createToken(data: dict):
    token:str=encode(payload=data, key="my_secre_key",algorithm="HS256")
    return token

def validateToken(token: dict)->dict:
    data:dict=decode(token, key="my_secre_key",algorithm=['HS256'])
    return data
