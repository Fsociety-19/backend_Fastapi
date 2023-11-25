from Data.conexion import Conexion
from Data.models.statusAppointModel import StatusAppointMent
class Status():
    def getAll():
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('SELECT * FROM statusappointments;')
                result=cursor.fetchall()
                payload=[]
                content={}
                for data in result:
                    content={
                        'id':data[0],
                        'name':data[1],
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
