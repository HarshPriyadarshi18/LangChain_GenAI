from typing import  TypedDict
from pydantic import BaseModel
class Student(BaseModel):
     name:str
class Person(TypedDict):
    name:str
    age:int
person = {'name':'John', 'age':25   }
#person2:Person = {'name':'John', 'age':'25'  }
print(person)
#print(person2)