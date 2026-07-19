

# global var - we can access but cant modify , to modify it we use use global var keyword 
# try above thing actually
# Every recursive function must have a base condition that stops the recursion or else the function calls itself infinitely.

# Modules 
# create module.
# try renaming of module alias 
# The from keyword lets you import only the names you need from a module into your current program.
# from math import *
# The dir() built-in function in modules 




# Package 
# package is a folder of modules 
# group of function, vars >> modules (single .py file )
# group of modules >> package 
# from package-name import specific-module
'''
mypackage/                ← this folder IS a package
│
├── __init__.py           ← marks the folder as a package
├── math_utils.py         ← a module inside the package
├── string_utils.py       ← another module
└── shapes/               ← a sub-package
    ├── __init__.py
    └── circle.py
'''


# Main function 
# python dont have main() function like other programming lang
# entrypoint - main with __name__




# ####################### Recursion ###################


def factorial(x):
    if x==1:
        return 1 
    else:
        return (x*factorial(x-1))

print(factorial(4))


