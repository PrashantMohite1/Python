

number = 7

for i in range(number+1):
    for j in range(i):
        print('*',end='')
    print()


# Reversed Stars 

for i in reversed(range(number+1)):
    for j in range(i):
        print('*',end='')
    print()
  
# optimise version of printing stars

for i in range(number):
    print(i * '*', end='')
    print()

for i in reversed(range(number)):
    print(i * '*', end='')
    print()