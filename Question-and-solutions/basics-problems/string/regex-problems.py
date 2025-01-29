
# Question 1 
"""
The validation rules are as follows:



The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
In any other case the string is not valid.


Example:

Input: 
str = asdsab@!@234
Output: 
True


Explanation: 
The string is valid as characters are
followed by special case characters 
which are then followed by numbers.


"""
import re


st1 = "asdsab@!@234"

pattern = r"[a-z]+[!@#$%]+[0-9]"

output = re.findall(pattern,st1)

print(output)

if output:
    print("yes matched")
else:
    print("No , Not Match")





# Question 2 

"""
In this question, we'll learn the use of Regex in Python. You will be provided a string str in which you have to find all the numbers and print them.

Note: In Python, you need to import re module to use regex

Example:

Input: 
str = asdasd123asmdasdk34234kfdsd34sdfk5
Output: 
123 34234 34 5

"""
str = "paras123chi12355"
pat=r"\d+"
match=re.findall(pat,str) ##find all finds all the matched texts and returns a list
if(match): 
    for i in match:
        print(i, end=" ")
else:
    print(-1,end="")