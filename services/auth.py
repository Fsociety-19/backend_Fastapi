from Data.conexion import Conexion
from Data.models.authModel import AuthModel
from fastapi import   HTTPException
from jwt_manager import createToken
class Auth():
    def doLogin(username,password):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('SELECT id,idTypeUser FROM users WHERE username=%s and password=%s',(username,password))
                result=cursor.fetchone()
                if result==None:
                    raise HTTPException(status_code=403,detail='Inicio fallido')
                else:
                    token=createToken(dict(id=result[0],rol=result[1]))
                    content={
                        'token_jwt':token,
                        'rol':result[1]
                    }
                cursor.close()
                conexion.close()
                return (content)
            except Exception as error:
                raise error
        else:
            return {"resultado":"Error desconocido.db"}
