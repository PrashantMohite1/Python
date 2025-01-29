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

- how to ignore Escape sequence 
    - by using r or R basically when we use r it consider given string in raw formate and ignore escape sequence
    ```
     str = r"\d+" 
    ```
       



### Imp Built in functions of string 

- title :
    this function return string in title formate in which it make first char to uppercase in word 
    ex- "hello world" = Hello World

- swapcase : 
    it makes string to opposit case 
    ex- "hello" = HELLO


- strip ():
    this function removes spaces from string 
    ex- "    hello   " = hello

    

- find("string", beg, end) :- This function is used to find the position of the substring within a string.It takes 3 arguments, substring , starting index( by default 0) and ending index( by default string length). 
 

    It returns "-1 " if string is not found in given range.
    It returns first occurrence of string if found.

- rfind("string", beg, end) :- This function has the similar working as find(), but it returns the position of the last occurrence of string.


- startswith("string", beg, end) :- The purpose of this function is to return true if the function begins with mentioned string(prefix) else return false.

- endswith("string", beg, end) :- The purpose of this function is to return true if the function ends with mentioned string(suffix) else return false.

- islower("string") :- This function returns true if all the letters in the string are lower cased, otherwise false.

- isupper("string") :- This function returns true if all the letters in the string are upper cased, otherwise false.


- lower() :- This function returns the new string with all the letters converted into its lower case.

- upper() :- This function returns the new string with all the letters converted into its upper case.

- swapcase() :- This function is used to swap the cases of string i.e upper case is converted to lower case and vice versa.

- title() :- This function converts the string to its title case i.e the first letter of every word of string is upper cased and else all are lower cased.
 

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

