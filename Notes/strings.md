# Strings 

In Python, Strings are arrays of bytes representing Unicode characters.


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

    
