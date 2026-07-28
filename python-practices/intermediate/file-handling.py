
import os 
import shutil

# get pwd , change directory, list directories
# make new dir, rename dir , 
# remove file or directory 

dir1 = r'C:\Users\mohit\personal-mydata\git\python-practices\docs'

print("PWD : ", os.getcwd())
os.chdir(r'C:\Users\mohit\personal-mydata\git\python-practices\docs')

print("PWD : ", os.getcwd())

shutil.rmtree(r'C:\Users\mohit\personal-mydata\git\python-practices\docs\temp')

print("LIST DIR : ", os.listdir(dir1))


# file = open('C:/Users/mohit/personal-mydata/git/python-practices/docs/file-encoding.md')
# file = open('C:/Users/mohit/personal-mydata/git/python-practices/docs/temp.txt', 'w+')

# file.write("THis is line written by program \nsecond line \n")
# file.write("third line \nfourth line")
# file.seek(0)

# file_read = file.read()
# print(file_read)