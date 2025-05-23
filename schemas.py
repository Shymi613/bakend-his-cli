from pydantic import BaseModel
from typing import List

class Allergy(BaseModel):
    id: int
    substance: str

    class Config:
        orm_mode = True

class History(BaseModel):
    id: int
    description: str

    class Config:
        orm_mode = True

class Medication(BaseModel):
    id: int
    name: str
    dosage: str

    class Config:
        orm_mode = True

class PatientDetail(BaseModel):
    id: int
    name: str
    allergies: List[Allergy]
    histories: List[History]
    medications: List[Medication]

    class Config:
        orm_mode = True