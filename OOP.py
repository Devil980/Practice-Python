class person:
    name = "Anish Timilsina"
    Class = 11
    Age = 17
    def info(self):
        print(f"{self.name} studies in class {self.Class} and his age is {self.Age}")
a = person()
b = person()
c = person()
a.name = "Hari Prasad"
a.Class = 12
a.Age = 18

b.name = "Ram Bahadur"
b.Class = 10
b.Age = 16
# print(a.name,a.Class,a.Age)
a.info()
b.info()
c.info()


class Employee:
    company = "Tesla"
    def __init__(self,name,):
        self.name = name
    def show(self):
        print(f"The name of the employee is {self.name} and he/she works in {self.company}")
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
e1 = Employee('Anish')
e2 = Employee('Hari')
e1.change_company('Facebook')
e1.show()
e2.change_company("Microsoft")
e2.show()
print(Employee.company)


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromstr(cls,string):
        name , salary = string.split("-")
        return cls(name , int(salary))
    
    def frompoi(cls,house):
        name , salary = house.split(",")
        return cls(name , int(salary))

e1 = Employee("Hari","100000")
print(e1.name,e1.salary)


string = "Anish-120000"
e2 = Employee.fromstr(string)
print(e2.name , e2.salary)

house = "Rohit,80000"
e3 = Employee.frompoi(house)
print(e3.name , e3.salary)


