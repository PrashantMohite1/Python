# Regex - Python

Regular expressions are extremely helpful in extracting useful information from loads of text. Regular expressions work on pattern-matching techniques. Extracting phone-number, validating passwords, and extracting images from web-pages are but a few examples of regex usage.

- while using "\\" , "\d+" for regex patter we will be getting syntax error because in string that consider as a escape sequence so as a solution we can ignore escape sequence using r or R because this r string cosiderd as raw string.

    ```
    ex - 
    pattern = r"\d+"
    ```

#### Process of using regular expression in python

- first need to import re
-  re.compile() function to create a regular expression object. 
- use several methods to search for and match patterns in strings. ex- match , search , findall , sub 


#### Builtin Functions For Regex

- compile :  
    re.compile() function to create a regular expression object. 
    re.compile() function takes a string as an argument and returns a regular expression object.


- match(): This method searches for a match at the beginning of the string.
- search(): This method searches for a match anywhere in the string.
- findall(): This method returns a list of all matches in the string.
- sub(): This method replaces all matches with a specified string.


#### Example of Regex


- find integers from string 
    ```
        import re 

        str1 = '''asdasd123asmdasdk34234kfdsd34sdfk5'''

        def numberMatcher(str):
            pat= r'\d+'
            match=re.findall(pat,str) 
            if(match): 
                for i in match:
                    print(i, end=" ")
            else:
                print(-1,end="")

        numberMatcher(str1)
    ```

