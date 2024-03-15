class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender
    def Introduce (self):
        return f"Hello,my name is {self.name},I am {self.age} years old and I am a {self.gender}"
My_details =Person("Nashon Omondi",18,"Male")
print(My_details.Introduce())