# class person:
#     name = "Anish Timilsina"
#     Class = 11
#     Age = 17
#     def info(self):
#         print(f"{self.name} studies in class {self.Class} and his age is {self.Age}")
# a = person()
# b = person()
# c = person()
# a.name = "Hari Prasad"
# a.Class = 12
# a.Age = 18

# b.name = "Ram Bahadur"
# b.Class = 10
# b.Age = 16
# # print(a.name,a.Class,a.Age)
# a.info()
# b.info()
# c.info()


# class Employee:
#     company = "Tesla"
#     def __init__(self,name,):
#         self.name = name
#     def show(self):
#         print(f"The name of the employee is {self.name} and he/she works in {self.company}")
#     @classmethod
#     def change_company(cls,new_company):
#         cls.company = new_company
# e1 = Employee('Anish')
# e2 = Employee('Hari')
# e1.change_company('Facebook')
# e1.show()
# e2.change_company("Microsoft")
# e2.show()
# print(Employee.company)


# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    
#     @classmethod
#     def fromstr(cls,string):
#         name , salary = string.split("-")
#         return cls(name , int(salary))
    
#     def frompoi(cls,house):
#         name , salary = house.split(",")
#         return cls(name , int(salary))

# e1 = Employee("Hari","100000")
# print(e1.name,e1.salary)


# string = "Anish-120000"
# e2 = Employee.fromstr(string)
# print(e2.name , e2.salary)

# house = "Rohit,80000"
# e3 = Employee.frompoi(house)
# print(e3.name , e3.salary)


# import qrcode as qr
# from PIL import Image
# url = input("Enter a url that you want to change into qr code: ")
# qr_code = qr.make(url)
# get_qr = qr_code.get_image()
# get_qr.show()
# import random
# import string

# def generate_password(length = 10):
#     passs = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(passs) for _ in range(length))
#     return password

# password  = generate_password()
# def save_password(password,filename="password.txt"):
#     with open(filename,"w") as file:
#         file.write(password)

# print("The generated password is: ",password)

# save_password(password)
# print("Password is saved to'password.txt")
# import os

# files = os.listdir("clutter")
# i = 1 
# for file in files:
#     if file.endswith(".png"):
#      print(file)
#      os.rename(f"clutter/{file}",f"clutter/.{i}.png")
#      i = i + 1
import turtle
def heart():
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.begin_fill()
    turtle.fillcolor("white")

    turtle.left(140)
    turtle.forward(224)
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224) 
    
    turtle.end_fill()  
    turtle.hideturtle()
    turtle.done()   
heart()