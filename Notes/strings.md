# Strings 

In Python, Strings are arrays of bytes representing Unicode characters.

Strings are immutable, hence elements of a String cannot be changed once it has been assigned. Only new strings can be reassigned to the same name. 


- String slicing - 
    ```
    sequence[start:stop:step]
    ```
- Reverse list - 
    ```
    gfg = "Hello World"
    print(gfg[::-1])

    ```
    or 
    ```
    gfg = "Hello World"
    gfg = "".join(reversed(gfg))
    print(gfg)
    ```

- Escape Sequencing in Python
    ```
    str = "prashant\n \"B\" Mohite"

    ```
- Triple quotes are also good way of escaping.
    ```
    test_str = """Prashant"B"Mohite"""

    ```





### Imp Built in functions of string 

- title , swapcase , find , strip

- title :
    this function return string in title formate in which it make first char to uppercase in word 
    ex- "hello world" = Hello World

- swapcase : 
    it makes string to opposit case 
    ex- "hello" = HELLO

- find():
    if we want to find how many times a char repeated in word then find will helpfull
    ex- hello = 2 

- strip ():
    this function removes spaces from string 
    ex- "    hello   " = hello

    
### Escape Characters 

-   '\n' --> Leaves a line
    '\t' --> Leaves a space

- Tripple coats '''Prashant Mohite''' : we can also use tripple coats for escape sequence but it is more easier that using \t \n \ of escape sequence. in tripple what ever convention we are giving it printed in that sense
    ```
    ex -:
    print('''Prashant        Mohite''')
    Output = Prashant       Mohite
    ```

- epr()  : This function returns a string in its printable  format, i.e doesn’t resolve the escape sequences.
    
    ```
    ch = "I\nLove\tIndia"
    print(repr(ch))

    output:
    'I\nLove\tIndia'

    ```

