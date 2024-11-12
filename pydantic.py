import re
from pydantic import BaseModel, EmailStr

#Using regular expression. 

email = "d@gmail.com"
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email address")
else:
  raise ValueError("Invalid email address")

#Using other method for data validation
age = "25"
if not age.isdigit():
    raise ValueError("Age must be an integer")
age = int(age)
print(age)

#Using pydantic to validate both age and email address. NB: we had to import EmailStr
class User(BaseModel):
  age: int
  email: EmailStr

user = User(age = 25, email="test_mail@gmail.com")
print(user)