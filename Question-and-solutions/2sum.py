
import numpy as np

nums = [2 , 7 , 11 , 15]
target = 9
myarray = np.array(nums)


indices = []
myarray_length = len(myarray)

print('list = ', nums)
print('myarray length ', len(myarray))


for j in myarray:
    n1 = target - j
    if n1 in nums and len(indices) != 2:
        indices.append(nums.index(n1))
print("indices = ", indices)



