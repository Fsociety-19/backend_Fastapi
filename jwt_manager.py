from jwt import encode,decode,exceptions

def createToken(data: dict):
    token:str=encode(payload=data, key="my_secre_key",algorithm="HS256")
    return token

def validateToken(token: dict)->dict:
    try:
        data:dict=decode(token, key="my_secre_key",algorithms=['HS256'])
        return data
    except exceptions.InvalidTokenError as e:
        raise NameError('ERROR EN EL TOKEN')
    
    
    
