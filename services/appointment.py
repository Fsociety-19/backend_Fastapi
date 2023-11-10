from Data.conexion import Conexion
from Data.models.appointmentModel import AppointMentModel
from Data.models.userdetailModel import UserDetailModel
class AppointMent():
    def getAll():   
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('''SELECT 
                               appointments.id,
                               appointments.reason,
                               appointments.idAdminStaff,
                               appointments.hour,
                               appointments.date,
                               statusappointments.name as "statusAppointMent",
                               appointments.detail,
                               appointments.idstudent,
                               detailuser.dni as "dni", 
                               detailuser.name as "name student", 
                               detailuser.lastName as "lastName student" 
                               FROM appointments INNER JOIN users ON users.id=appointments.idstudent INNER JOIN detailuser ON detailuser.id=users.id INNER JOIN statusappointments ON statusappointments.id=appointments.idStatusAppointment ORDER BY appointments.date DESC;''')
                result=cursor.fetchall()
                payload=[]
                content={}
                for data in result:
                    content={
                        'id':data[0],
                        'reason':data[1],
                        'idAdmin':data[2],
                        'hour':data[3],
                        'date':data[4],
                        'status':data[5],
                        'detail':data[6],
                        'student':{
                            'idStudent':data[7],
                            'dni':data[8],
                            'name':data[9],
                            'lastName':data[10],
                        }
                        
                    }
                    payload.append(content)
                    content={}
                cursor.close()
                conexion.close()
                if payload is None or payload==[]:
                    return{"resultado":"No hay registros"}
                else:
                    return (payload)
            except Exception as error:
                return {"resultado":"error: "+str(error),}
        else:
            return {"resultado":"Error desconocido.db"}
    def getCount():   
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('''SELECT  COUNT(id) FROM appointments;''')
                result=cursor.fetchall()
                payload=[]
                content={}
                for data in result:
                    content={
                        'total':data[0],
                    }
                    payload.append(content)
                    content={}
                cursor.close()
                conexion.close()
                if payload is None or payload==[]:
                    return{"resultado":"No hay registros"}
                else:
                    return (payload)
            except Exception as error:
                return {"resultado":"error: "+str(error),}
        else:
            return {"resultado":"Error desconocido.db"}   
    def create(appointment:AppointMentModel):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute("INSERT INTO appointments (reason, idstudent, detail) VALUES(%s,%s,%s)",(appointment.reason,appointment.idStudent,appointment.detail,))
                conexion.commit()
                cursor.close()
                return {"Informacion":"Informe Registrado"}
            except Exception as error:
                return {"resultado":"error"}
        else:
            return {"resultado":"Error desconocido.db"}
    def getOne(id:int):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('''SELECT 
                               appointments.id,
                               appointments.reason,
                               appointments.idAdminStaff,
                               appointments.hour,
                               appointments.date,
                               statusappointments.name as "statusAppointMent",
                               appointments.detail,
                               appointments.idstudent,
                               detailuser.dni as "dni", 
                               detailuser.name as "name student", 
                               detailuser.lastName as "lastName student" 
                               FROM appointments 
                               INNER JOIN users ON users.id=appointments.idstudent 
                               INNER JOIN detailuser ON detailuser.id=users.id 
                               INNER JOIN statusappointments ON statusappointments.id=appointments.idStatusAppointment 
                               WHERE appointments.id= %s ''',(id,))
                result=cursor.fetchall()
                payload=[]
                content={}
                for data in result:
                    content={
                        'id':data[0],
                        'reason':data[1],
                        'idAdmin':data[2],
                        'hour':data[3],
                        'date':data[4],
                        'status':data[5],
                        'detail':data[6],
                        'student':{
                            'idStudent':data[7],
                        'dni':data[8],
                        'name':data[9],
                        'lastName':data[10],
                        }
                        
                    }
                    payload.append(content)
                    content={}
                if payload is None or payload==[]:
                    return{"resultado":"Reserva no encontrada"}
                else:
                    return (payload)
            except Exception as error:
                return {"resultado":"error: "+str(error),}
        else:
            return {"resultado":"Error desconocido.db"}
    def update(id:int,data:AppointMentModel):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('UPDATE appointments SET detail=%s,idStatusAppointment=%s,idAdminStaff=%s  WHERE id=%s',(data.detail,data.idStatusAppointment,data.idAdminStaff,id))
                conexion.commit()
                cursor.close()
                return {"informacion":"Detalles de reserva actualizados"}
            except Exception as error:
                return {"resultado":"error: "+str(error),}
        else:
            return {"resultado":"Error desconocido.db"}
    def delete(id:int):
        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('DELETE FROM appointments WHERE id=%s',(id,))
                conexion.commit()
                cursor.close()
                return {"informacion":"Registro eliminado"}
            except Exception as error:
                return {"resultado":"error: "+str(error),}
        else:
            return {"resultado":"Error desconocido.db"}

        conexion=Conexion.create()
        if conexion.is_connected():
            try:
                cursor=conexion.cursor()
                cursor.execute('DELETE FROM userdetail WHERE id=%s',(id))
                conexion.commit()
                cursor.close()
                return {"informacion":"Informacion de Usuario eliminada"}
            except Exception as error:
                return {"resultado":"error: "+error,}
        else:
            return {"resultado":"Error desconocido.db"}
    