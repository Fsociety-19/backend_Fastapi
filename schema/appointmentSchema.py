from pydantic import BaseModel
class CreateAppointment(BaseModel): 
		reason: str
		detail: str
	

class UpdateAppointment(BaseModel):
		idAdmin:int
		status: int
		detail: str       
