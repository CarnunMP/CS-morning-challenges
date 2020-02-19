### Objective challenge:
### Given an image represented by an NxN matrix, where each pixel in the image is an integer from 0 to 9, write a function rotate_image that receives a matrix as input and rotates the image by 90 degrees in the counter-clockwise direction.

### Objective challenge:
### Classify the runtimes of each of the following functions:

### 1.
### def foo(n):
###   sq_root = int(math.sqrt(n))
###   for i in range(0, sq_root):
###     print(i)

# It's not constant, because as n grows so does the printed list. But it's not quite linear either. So: O(log(n))

### 2.
### def bar(x):
###   sum = 0
###   for i in range(0, 1463): # Constant
###     i += sum
###     for j in range(0, x): # 1463 x-length loops
###       for k in range(x, x + 15): # Constant
###         sum += 1

# Looks linear to me! O(n)

### 3.
### def baz(array):
###   print(array[1]) # O(1)
###   midpoint = len(array) // 2
###   for i in range(0, midpoint): O(n)
###     print(array[i]) # O(1)
###   for _ in range(1000): # Constant, O(1)
###     print('hi')

# O(n)
