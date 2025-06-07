from fastapi import FastAPI
from pydantic import BaseModel

from lesson22.api_development.client import response

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str


class Person(BaseModel):
    name: str
    age: int

class ResponsePerson(BaseModel):
    message: str


@app.post("/create_person")
async def create_person(person: Person):
    return {"message:" f"Person{person.name} created with age {person.age}"}

@app.post("/users/")
async def create_user(user: User):
    return user

@app.post("/create_person/", response_model=ResponsePerson)
async def create_person(person: Person):
    return {"message:" f"Person{person.name} created with age {person.age}"}