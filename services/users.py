from Data.conexion import Conexion
from Data.models.userModel import UserModel
from Data.models.userdetailModel import UserDetailModel
class User():
    def getAllDetail():
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('SELECT * FROM users INNER JOIN detailuser ON users.id=detailuser.idUser ORDER BY detailuser.name;')
                result=cursor.fetchall()
                payload=[]
                content={}
                for data in result:
                    content={
                        'id':data[0],
                        'username':data[1],
                        'idRol':data[3],
                        'detalle':{
                            'dni':data[5],
                            'fullname':data[6]+" "+data[7],
                        }
                    }
                    payload.append(content)
                    content={}
                cursor.close()
                conexion.close()
                return (payload)
            except Exception as error:
                return {"resultado":"error: "+error,}
        else:
            return {"resultado":"Error desconocido.db"}
    def getAll():
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('SELECT * FROM users;')
                result=cursor.fetchall()
                payload=[]
                content={}
                for data in result:
                    content={
                        'id':data[0],
                        'username':data[1],
                        'idRol':data[3],
                    }
                    payload.append(content)
                    content={}
                cursor.close()
                conexion.close()
                return (payload)
            except Exception as error:
                return {"resultado":"error: "+error,}
        else:
            return {"resultado":"Error desconocido.db"}
    def create(User:UserModel):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute("INSERT INTO users (username, password, idRol) VALUES(%s,%s,%s)",(User.username,User.password,User.idRol))
                conexion.commit()
                cursor.close()
                return {"Informacion":"Usuario Registrado"}
            except Exception as error:
                return {"resultado":"error"}
        else:
            return {"resultado":"Error desconocido.db"}
    def getAdmins():
            conexion=Conexion.create()
            if conexion.is_connected():
                try:
                    cursor=conexion.cursor()
                    cursor.execute('SELECT us.id,det.name,det.lastName FROM users us JOIN detailuser det ON det.idUser=us.id WHERE us.idTypeUser=2')
                    result=cursor.fetchall()
                    payload=[]
                    content={}
                    for data in result:
                        content={
                            'id':data[0],
                            'name':(data[1]+" "+data[2]),
                        }
                        payload.append(content)
                        content={}
                    cursor.close()
                    conexion.close()
                    if payload is None or payload==[]:
                        return{"resultado":"Usuario no encontrado"}
                    else:
                        return (payload)    
                except Exception as error:
                    return {"resultado":"error: "+str(error),}
            else:
                return {"resultado":"Error desconocido.db"}                
    def getOne(id:int):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('SELECT * FROM users WHERE id = %s',(id,))
                result=cursor.fetchall()
                payload=[]
                content={}
                for data in result:
                    content={
                        'id':data[0],
                        'username':data[1],
                        'idRol':data[3]
                    }
                    payload.append(content)
                    content={}
                cursor.close()
                conexion.close()
                if payload is None or payload==[]:
                    return{"resultado":"Usuario no encontrado"}
                else:
                    return (payload)    
            except Exception as error:
                return {"resultado":"error: "+str(error),}
        else:
            return {"resultado":"Error desconocido.db"}
    def findOne(name:str):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute("SELECT * FROM detailuser WHERE name like %s",(str("%"+name+"%"),))
                result=cursor.fetchall()
                payload=[]
                content={}
                for data in result:
                    content={
                        'id':data[0],
                        'dni':data[1],
                        'name':data[2],
                        'lastname':data[3],
                        }
                    payload.append(content)
                    content={}
                cursor.close()
                conexion.close()
                if payload is None or payload==[]:
                    return {"resultado":"No hay concidencias"}
                else:
                    return (payload)
            except Exception as error:
                return {"resultado":"error: "+str(error),}
        else:
            return {"resultado":"Error desconocido.db"}
    def update(id:int,data:UserDetailModel):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('UPDATE detailuser SET dni=%s,name=%s,lastName=%s WHERE idUser=%s',(data.dni,data.name,data.lastName,data.idUser))
                conexion.commit()
                cursor.close()
                return {"informacion":"Detalles de usuario actualizado"}
            except Exception as error:
                return {"resultado":"error: "+error,}
        else:
            return {"resultado":"Error desconocido.db"}
    def deleteUser(id:int):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('DELETE FROM users WHERE id=%s',(id,))
                conexion.commit()
                cursor.close()
                return {"informacion":"Usuario eliminado"}
            except Exception as error:
                return {"resultado":"error: "+str(error),}
        else:
            return {"resultado":"Error desconocido.db"}
    def deleteUserDetail(id:int):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('DELETE FROM detailuser WHERE id=%s',(id,))
                conexion.commit()
                cursor.close()
                return {"informacion":"Informacion de Usuario eliminada"}
            except Exception as error:
                return {"resultado":"error: "+str(error),}
        else:
            return {"resultado":"Error desconocido.db"}
    def deleteUserDetailByLike(like:str):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute("SELECT * FROM detailuser WHERE name like %s",(str("%"+like+"%"),))
                conexion.commit()
                cursor.close()
                return {"informacion":"Informacion de Usuario eliminada"}
            except Exception as error:
                return {"resultado":"error: "+str(error),}
        else:
            return {"resultado":"Error desconocido.db"}
    