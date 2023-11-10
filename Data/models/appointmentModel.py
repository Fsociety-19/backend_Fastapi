class AppointMentModel:
    def __init__(self,idStudent=None,reason=None,detail=None,hour=None,date=None,idStatusAppointment=None,idAdminStaff=None,id=None):
        self.id=id
        self.reason=reason
        self.idStudent=idStudent
        self.idAdminStaff=idAdminStaff
        self.hour=hour
        self.date=date
        self.idStatusAppointment=idStatusAppointment
        self.detail=detail
        

