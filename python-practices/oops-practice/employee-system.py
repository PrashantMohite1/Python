from abc import ABC, abstractmethod

class employee(ABC):
    def __init__(self, name, age, department,salary):
        self.name = name 
        self.age = age 
        self.department = department
        self.__salary = salary

    def emp_details(self):
        return f"Name :  {self.name}, Age : {self.age}, Department : {self.department} "

    def get_salary(self):
        return f"Salary : {self.__salary}"

    @abstractmethod 
    def work():
        pass

class developer(employee):
    def work(self):
        return "Contribute in software lifecycle, resolve bugs , deploy new code"


class hr(employee):    

    def work(self):
        return f"Hire new employees\ncheck employee salary \nplan company trips"
    
    def hire_empl(self,name, age, department,salary):
        emp = developer(name, age, department,salary)
        return emp

hr1 = hr("jayashree",30, "HR",20000)

dev1 = hr1.hire_empl("prashant",24,"developer", 30000)

print("HR Salary : " , hr1.get_salary())
print("HR Details : " , hr1.emp_details())
print("New Employee : " , dev1.emp_details())







