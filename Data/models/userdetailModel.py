class UserDetailModel:
    def __init__(self,dni,name,lastName,idUser,id=None):
        self.id=id
        self.dni=dni
        self.name=name
        self.lastName=lastName
        self.idUser=idUser