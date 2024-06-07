# def cube(x):
#     return x * x *x
# l = [2,4,5,6,7,8]
# ll = [32]
# newl=list(map(lambda x: x*x*x,l))
# print(newl)
# def filter_python(a):
#     return a<4
# newnewl = list(filter(filter_python,l))
# print(newnewl)
# from functools import reduce
# # def sum(x,y):
# #     return x+y
# red = reduce(lambda x,y: x+y,l)
# print(red)
# a = input("Enter Your Name: ")
# print("your name is ",a)
# import logging

# logging.basicConfig(level=logging.INFO)

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a + b
# my_function(1,2)
# def greet(fx):
#     def mfx(*args, **kwargs):
#      print("welcome to the program")
#      result = fx(*args, **kwargs)
#      print("Thanks for using the program")
#      return result
#     return mfx

# @greet
# def add(a,b):
#     print(a+b) 
# result = add(5,6)
# print(result)

# def namaste(fx):
#    def mfx(*args,**kwargs):
#       print("Long Time No see")
#       result = fx(*args,**kwargs)
#       print("Its great to see you")
#       return result
#    return mfx
# @namaste
# def hello():
#    print("Hello man whats up! ")
# message = hello()
# print(message)
# @greet
# def add(a,b):
#     print(a+b) 
# add(5,6)

# class Employee():
#     def __init__(self,name,post):
#         self.name = name
#         self.post = post
#     def showdetails(self):
#      print(f"The name of the employee is {self.name} and his/her post is {self.post}")
# class Extra_skill(Employee):
#    def programmer(self):
#     print("His,Her extra skill is Singing  ")

# e = Extra_skill("Anish Timilsina","HR")
# e.showdetails()
# e.programmer()
def Fractional(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*Fractional(n-1)
print(Fractional(5))
    