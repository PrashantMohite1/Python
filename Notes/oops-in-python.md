

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

