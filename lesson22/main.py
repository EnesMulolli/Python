from pydantic import BaseModel, conint, constr
from typing import Optional

# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str

#
# user = User(id=1, name='John', age=25, email='john@gmail.com')
# print(user)



class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None

user1 = User(id=1, name='John', age=25)
print(user1)

user2 = User(id=2, name='William')
print(user2)

user3 = User(id=3, name='James', age=30, email='james@gmail.com')
print(user3)





class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=55)

valid_user = another_user(id=1, name='John')
print(valid_user)

# invalid_user = another_user(id=0, name='J')
# print(invalid_user)



