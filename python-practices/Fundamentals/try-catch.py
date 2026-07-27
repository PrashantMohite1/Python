

# simple try catch.
# catch specific exception.
# try with else cause - some situation where we just dont want to show error instead perform some logic based on it
# try with finally.




try : 
    divideby = int(input("Enter Divideby 10 number : "))
    out = 10/divideby
except ZeroDivisionError :
    print("We can't divide by zero")
else:
    print("Running Else : output = ", out)
finally:
    print("Running Finally block ")



print("Line of code after the exception")