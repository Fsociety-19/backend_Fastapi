from pydantic import BaseModel
class CreateAppointment(BaseModel): 
		reason: str
		detail: str
		idStudent: int
	

class UpdateAppointment(BaseModel):
		idAdmin:int
		status: int
		detail: str       
