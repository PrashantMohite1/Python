

i1 = str(input("Enter your Name "))

dic1 = {}

print(type(dic1))

l2 = i1.split(" ")

if l2[0] == 'i' :
    dic1[l2[1]] = l2[2]



print("Dict = ", dic1)