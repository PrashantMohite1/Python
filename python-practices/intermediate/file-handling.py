
import os 
import shutil

# get pwd , change directory, list directories
# make new dir, rename dir , 
# remove file or directory 
file1 = r'C:\Users\mohit\personal-mydata\git\python-practices\docs\temp.txt'

dir1 = r'C:\Users\mohit\personal-mydata\git\python-practices\docs'

print("PWD : ", os.getcwd())
os.chdir(r'C:\Users\mohit\personal-mydata\git\python-practices\docs')

print("PWD : ", os.getcwd())

# to delete directory 

# shutil.rmtree(r'C:\Users\mohit\personal-mydata\git\python-practices\docs\temp')



# list dir 
print("LIST DIR : ", os.listdir(dir1))


with open(file1, 'w+') as f1:
    f1.write("PPPPPPPPPPPPPPPrashant")
    f1.seek(0)
    print(f1.read())


# file = open('C:/Users/mohit/personal-mydata/git/python-practices/docs/file-encoding.md')
# file = open('C:/Users/mohit/personal-mydata/git/python-practices/docs/temp.txt', 'w+')

# file.write("THis is line written by program \nsecond line \n")
# file.write("third line \nfourth line")
# file.seek(0)

# file_read = file.read()
# print(file_read)