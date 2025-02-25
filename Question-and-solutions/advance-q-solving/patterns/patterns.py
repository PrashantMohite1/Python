


"""
*****
*****
*****
*****
*****

"""


# row = 5 , col = 5

def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*', end = "")
        print()


# pat 2

"""
*
**
***
****
*****
"""

# row = 5                             ## columns = 1 ,2 3, 4 , 5

def pattern2(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end="")
        print()

        # or 
    # for i in range(row + 1):
    #     pattern = i * '*'
    #     print(pattern)






"""
1
12
123
1234
12345
"""



# rows = 5

# i = 1
# for i in range(rows + 2):
#     j = 1
#     while j < i :
#         # print(f"value of i {i} value of j = {j}" )
#         print(j, end="")
#         j +=1 
#     print("")

"""
1
22
333
4444
55555
"""
# row = 5                    #columns = 1 , 2 , 3, 4 , 5

# i = 1
# for i in range(row+1):

#     for j in range(i):
#         print(i , end = '')
#     print()


"""
12345
1234
123
12
1
"""


# # rows = 5 ,   # columns - 5 , 4 , 3 , 2 ,1
# rows = 5


# for i in range(rows):
#     result = rows - i
#     for j in range(1, result+1):
#         print(j , end='')
#     print()



# 9,7,5,3,1


# pattern 7
"""
    *
   ***
  *****
 *******
*********

"""


def pattern7(n):
    
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        
        for k in range(i * 2 +1):
            print("*", end="")


#  or 

def pat7_math_approach(n):
    for i in range(n):
        spaces = (n-i-1)
        stars = (i * 2 + 1)
        print(spaces * " " + stars * '*' )

# pattern 8

"""
*********
 *******
  *****
   ***
    *
"""

def pattern8(n):
    for i in range(n):
        
        # print(f"value of i = {i}")
        for j in range(i):
            print("",end=" ")

        stars = ((n-i)*2) - 1
        for k in range(stars):
            print('*',end="")
        print()


# pattern 9

"""
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
"""

def pattern9(n):


    for i in range(n):
        for j in range(n-i-1):
            print("", end = " ")
        
        for k in range(i*2 + 1):
            print("*", end="")
        print()

    for i in range(n):
        
        # print(f"value of i = {i}")
        for j in range(i):
            print("",end=" ")

        stars = ((n-i)*2) - 1
        for k in range(stars):
            print('*',end="")
        print()





# pattern 10

"""

*
**
***
****
*****
****
***
**
*

"""

def pattern10(n):
    for i in range(n+1):
        for j in range(i):
            print('*', end="")
        print()

    for i in range(n+1):
        for k in range(n-i-1):
            print("*", end="")
        print()



"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""
def pattern11(n):
    start = 1
    for i in range(n+1):

        if i%2 == 0 :
            # print(f"i = {i}")
            start = 0 
        else:
            start = 1
        
        for j in range(i):
            # print(f"i = {i}")
            print(start ,end="")
            start = 1 - start
        print()
        

"""

1      1
12    21
123  321
12344321

"""


def pattern12(n):
    for i in range(1,n+1):

        # 1st numbers
        for j in range(1,i+1):
            print(j , end="")

        # spaces 

        spaces = (n -i )* 2

        for l in range(spaces):
            print("", end=" ")
        

        # 3rd numbers

        for k in range(i,0,-1):
            print(k ,end="")
        print()



"""
1
23
456
789
11 12 13 14 15

"""

def pattern13(n):
    num = 1
    for i in range(n+1):
        for j in range(i):
            print(num , end="")
            num = num+1

        print()


if __name__ ==  "__main__":
    n = int(input("Enter Value of N : "))  
    pattern13(n)
   
    