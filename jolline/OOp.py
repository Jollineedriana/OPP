#User class with properties name, age, location
class Users:
    name= "Jolline"
    age= 20
    location= "Kireka"
user1= Users()
print(user1.name)
print(user1.age)
    
    

class User:
    def __init__(self, name, age, location):
        self.name= name
        self.age= age
        self.location= location
User1= User("Namukose Jolline",20, "Kireka")

print(User1.name)
print(User1.age)
print(User1.location)