import numpy as np

arr = np.array([[2,4],[6,8]])
print(arr[0][1]) # will print the elements from 3 to 5

arr[1][1] = 1000

print(arr)
#print(arr[:5]) # will print the elements from 0 to 4
