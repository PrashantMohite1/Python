
# ########## Functions 

# create func & call 
# func with argument
#  funct which take two input and prints out with addition 

# parameter vs argument,  func temp(name){}   , temp("prashant")   so here name is parameter and "prashant" is the argument
# func with return statement
# pass is used in function when we have planned to implement the function but right now dont want to anything to body of function

# default argument in the function fun( defaultarg=10)




# Python Function arguments 
# arg with default values , for this test with passing no values, passing with values.
# arbitrary Arguments - *args 

# *args and **kwargs

'''
Types of arguments 

positional args : func person(name, age) { ) , person ( "prashant", 26) here we mentioned positional args 
keyword args : func person ( age , name ) {}, person(name="prashant", age = 26 ) here we mentioned keyword args 

*args = when we dont want to limit position arguments or we dont know how much positional args will be passed 
**kwargs = when we dont know about how much keyword arguments will be passed 

Caller passes keyword arguments (key=value) → **kwargs receives them as a dictionary.

*args
Collects extra positional values into a tuple.

Collects extra key=value options into a dictionary.

Use *args when you're processing many values of the same type (ports, file paths, IP addresses, numbers, services).
Use **kwargs when you're accepting configuration or options (region, instance type, timeout, retries, namespace, tags, headers, etc.). That's why you'll see **kwargs much more often than *args in SDKs, automation libraries, and frameworks
'''



# variable scope - 
# local - accessible in defined function 
# global - accessible across all the function 
# nonlocal- it means use existing var from nearest enclosing function 

# non-local 
'''
def outer():
    x = 10

    def inner():
        nonlocal x         # if we comment out this line - our outer var cant changed because inner will create new var here we are 
                           # we are saying dont create local var use nonlocal var 
        x = 20

    inner()
    print(x)

outer()
'''




def greet():
    print("hello, how are you")


def greetv2(name):
    # print("Hey %s, whats up!" % (name))
    # or 
    print(f"Hey {name}, how are you!")

greet()
greetv2("rakesh")


def addfun(n1, n2):
    out = n1+n2
    return out
output = addfun(2,3)

print("the sum is : ", output)

# defualt argument function 

def argtest(name="prashant", age=20):
    print(name, age)

argtest()
argtest("rakesh")
argtest("rakesh", 27)



def lstnames(*names):
    print("Printing list of arguments")
    for i in names:
        print(i)

lstnames("prashant",9 , 10, "sanaths")

def name_age(name, **subjects):
    print(name)
    print(subjects)

name_age(name= "prashant", math= 50 , english=56)

def pizza(size, **ingredient):
    print(size)
    print("Ingredients : ", ingredient)

pizza("large", spice_level="high", extra="cheese")