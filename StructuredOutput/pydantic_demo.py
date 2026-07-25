from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=7)

new_student = {
    'name': 'Alice',
    'email': 'alice@example.com', 
    'cgpa': 8.5
}

student_instance = Student(**new_student)
print(student_instance)