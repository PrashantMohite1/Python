

# Oops in Python 


### object and classes

**Class:**
- A class is like a blueprint or template. It defines what an object of that type should look like (its attributes) and what it should be able to do (its methods). It doesn't represent a real object yet, it just describes how the object should behave.

- Attributes are like properties or characteristics of the object.
Methods are actions or functions that the object can perform.

- `__init__(self)`: This is a special method known as the constructor. It initializes the object's attributes when an object of the class is created.


-   ```
    # class syntax 

    class ClassName:
    def __init__(self, parameters):  # Constructor (initializer)
        self.attribute = value         # Instance attribute

    def method(self):
        # Method to perform an action
        print("This is a method of the class.")


    ```


**Object:**
- An object is a real instance of a class. Once you create an object from a class, it actually exists in memory. The object can use the attributes and methods defined in the class.

- Attributes in the object store the real data.

- When an object of a class is created, the class is said to be instantiated.

    ```
    class Car:
        def __init__(self, make, model, year):
            self.make = make     # Instance attribute
            self.model = model   # Instance attribute
            self.year = year     # Instance attribute

        def description(self):
            # Method that describes the car
            return f"{self.year} {self.make} {self.model}"

    my_car = Car("Toyota", "Corolla", 2020)

    ```



### constructor 

are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the `__init__()` method is called the constructor and is always called when an object is created.



Types of constructors :

- Default constructor:

    The default constructor is a simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.

    ```
    def __init__(self):
    # body of the constructor`

    ```

- Parameterized constructor:

    constructor with parameters is known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

    ```
    def __init__(self, f, s):

        self.first = f
        self.second = s

    ```


### Destructors

Destructors are called when an object gets destroyed. In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically.

The `__del__()` method is a known as a destructor method in Python. It is called when all references to the object have been deleted i.e when an object is garbage collected.




## Inheritance


Inheritance is a fundamental concept in Python programming. It is primarily used to implement an is-a relationship among classes, promoting code reuse. This means that you can create a new class based on an existing class, inheriting its attributes and methods.

Benefits of Inheritance :
    The main advantage of inheritance is the ability to reuse code. This reduces redundancy and makes maintenance easier. For example, if you need to update a common feature, you only have to do it in one place instead of multiple classes.

```
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Employee(Person):
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary

    def printDetails(self):
        print(self.id)
        print(self.name)
        print(self.salary)

e = Employee(101, "Rahul", 40000)
e.printDetails()
```






### **Link between Access Modifiers and Encapsulation in Python**

In **encapsulation**, we hide the internal details of a class and only expose the necessary parts of the object. **Access modifiers** are tools used to control the level of access to the data (attributes) and methods of a class, which is crucial for implementing encapsulation.

Access modifiers allow you to decide:
- Which parts of a class can be accessed from outside the class.
- Which parts of a class are **protected** or **private**, meaning they can’t be modified directly.

### **Types of Access Modifiers in Python**

Python doesn't have strict access modifiers like some other languages (e.g., Java), but it follows naming conventions to indicate the level of access. There are three main types:

1. **Public Access Modifier** (Default)
2. **Protected Access Modifier**
3. **Private Access Modifier**

### 1. **Public Access Modifier** (Default in Python)
By default, all attributes and methods in a Python class are **public**, meaning they can be accessed directly from outside the class.

- **Public** attributes and methods can be accessed directly without any restrictions.

**Example:**

```python
class Car:
    def __init__(self, model, color):
        self.model = model  # public attribute
        self.color = color  # public attribute

    def display_info(self):  # public method
        print(f"Model: {self.model}, Color: {self.color}")

# Create an object of the Car class
car1 = Car("Toyota", "Red")

# Accessing public attributes directly
print(car1.model)  # Output: Toyota
print(car1.color)  # Output: Red

# Accessing public method
car1.display_info()  # Output: Model: Toyota, Color: Red
```

### 2. **Protected Access Modifier**
In Python, attributes or methods that start with a **single underscore** (`_`) are considered **protected**. This is more of a convention to indicate that these attributes or methods should not be accessed directly outside the class or its subclasses. However, it is **not enforced by Python** (i.e., you can still access them if needed).

- **Protected** attributes are intended to be accessed only within the class or by subclasses.

**Example:**

```python
class Car:
    def __init__(self, model, color):
        self._model = model  # protected attribute
        self._color = color  # protected attribute

    def _display_info(self):  # protected method
        print(f"Model: {self._model}, Color: {self._color}")

# Create an object of the Car class
car1 = Car("Honda", "Blue")

# Accessing protected attributes and methods (not recommended)
print(car1._model)  # Output: Honda
car1._display_info()  # Output: Model: Honda, Color: Blue
```

### 3. **Private Access Modifier**
In Python, attributes or methods that start with **double underscores** (`__`) are considered **private**. These cannot be accessed directly from outside the class. Python uses **name mangling** to make the attribute harder to access by changing its name internally.

- **Private** attributes are meant to be used only inside the class.

**Example:**

```python
class Car:
    def __init__(self, model, color):
        self.__model = model  # private attribute
        self.__color = color  # private attribute

    def __display_info(self):  # private method
        print(f"Model: {self.__model}, Color: {self.__color}")

# Create an object of the Car class
car1 = Car("BMW", "Black")

# Trying to access private attributes directly will result in an error
# print(car1.__model)  # This will raise an AttributeError

# However, you can still access the private attribute through name mangling (not recommended)
print(car1._Car__model)  # Output: BMW
```

### **Summary of Access Modifiers:**

1. **Public**: 
   - No underscores (`self.attribute`).
   - Can be accessed from outside the class directly.
2. **Protected**: 
   - Single underscore (`_self.attribute`).
   - Meant for internal use (class or subclasses).
3. **Private**: 
   - Double underscores (`__self.attribute`).
   - Cannot be accessed directly from outside the class (name mangling).

### **Why are Access Modifiers Important for Encapsulation?**

- **Encapsulation** is about hiding the internal state of an object and exposing only the necessary parts.
- **Access modifiers** help to control the visibility and accessibility of an object's attributes and methods, ensuring that the internal state is protected from unwanted changes or misuse.