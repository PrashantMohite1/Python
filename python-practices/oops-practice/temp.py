from abc import ABC, abstractmethod


class employee(ABC):
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.__salary = salary

    def emp_details(self):
        return f"Name : {self.name}, Age : {self.age}, Department : {self.department}"

    def get_salary(self):
        return f"Salary : {self.__salary}"

    @abstractmethod
    def work(self):
        pass


class developer(employee):
    def work(self):
        return "Contribute in software lifecycle, resolve bugs, deploy new code"


class hr(employee):
    # registry of roles HR is allowed to hire
    _roles = {}

    def work(self):
        return "Hire new employees\ncheck employee salary\nplan company trips"

    def hire(self, role, name, age, salary):
        """HR is the factory: creates and returns a new employee."""
        role_class = hr._roles.get(role)
        if role_class is None:
            raise ValueError(f"HR cannot hire unknown role: {role}")
        new_emp = role_class(name, age, department=role, salary=salary)
        print(f"{self.name} (HR) hired {name} as {role}")
        return new_emp


# register the roles HR can create
hr._roles = {
    "developer": developer,
}


# --- usage ---
recruiter = hr("Prashant", 26, "HR", 10000)

dev = recruiter.hire("developer", "Aman", 24, 50000)
print(dev.emp_details())
print(dev.work())