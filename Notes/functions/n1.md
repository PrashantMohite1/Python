

## Python Functions




- #### Types of Arguments In Function
 
  - Python supports various types of arguments that can be passed at the time of the function call. Let’s discuss each type in detail.


  - Default Arguments 
    A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
    ex- def myFun(x, y=50): print (x , y)

  - **Variable-length arguments** :- 
  In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:

  1. *args (Non-Keyword Arguments) : def nkey(*pm): for i in pm: print(pm)
  2. **kwargs (Keyword Arguments) :
      ```
      def fun(*args, **kwargs):
      print("Positional arguments:", args)
      print("Keyword arguments:", kwargs)

      fun(1, 2, 3, a=4, b=5)

      ```
- **Docstring** :- The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.
- **Return Statement** :- The function return statement is used to exit from a function and go back to the function caller and return the specified value or data item to the caller.

- **Anonymous functions**: In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions
- **Nested Fuctions** : A function that is defined inside another function is known as the inner function or nested function. Nested functions are able to access variables of the enclosing scope. Inner functions are used so that they can be protected from everything happening outside the function.
- **pass** -: The pass statement is a null statement. But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored.
- **yield** :- The yield keyword is used in Python to make a function generate a value and then pause its execution, allowing it to resume later. It's like a "return" statement, but instead of exiting the function, it allows the function to continue from where it left off the next time it's called.

  When a function contains yield, it is called a generator function. A generator function returns a generator object, which can be iterated over (like a list) one value at a time.

#### Module 
---
A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.

- **import** statement used to import any python file 
```
  import calcifile 
  print(calcifile.sum_item(3,4))
```

- **The from import Statement** - Python’s from statement lets you import specific attributes from a module without importing the module as a whole.
```
  from calicifile import sum_items, sub_items
  print(sum_items(10,20))
```
- **renaming module** :- import math as gfg



### Garbage Collection in Python

#### Reference counting
Python keeps track of how many references (or pointers) there are to each object. When an object’s reference count drops to zero (meaning no part of the program is using it anymore), Python automatically deletes that object and frees the memory.





#### Reference Cycles
While reference counting works in most cases, there’s a problem with cyclic references. This happens when two or more objects reference each other, forming a cycle. In this case, their reference counts never drop to zero, even though they are no longer in use.

To handle reference cycles, Python includes a garbage collector (GC) that periodically looks for and cleans up objects that are part of reference cycles. It does this using a more advanced algorithm, which can detect and break cycles.