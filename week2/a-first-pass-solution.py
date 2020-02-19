### Objective challenge:
### Given an image represented by an NxN matrix, where each pixel in the image is an integer from 0 to 9, write a function rotate_image that receives a matrix as input and rotates the image by 90 degrees in the counter-clockwise direction.

# You can think of such a rotation as the composition of two relfections: about the y-axis, then the line y = -x.
# So:

def rotate_cc(image_matrix):
    # I'm assuming image_matrix looks something like [[a b c d],
    #                                                 [e f g h],
    #                                                 [i j k l],
    #                                                 [m n o p]]                                

    # Reflection about the y-axis is like swapping opposite columns:
    for i in range(len(image_matrix) // 2):
        columnA = [row[i] for row in image_matrix]
        columnB = [row[len(image_matrix) - 1 - i] for row in image_matrix]

        for j in range(len(image_matrix)):
            image_matrix[j][i] = columnB[j]
            image_matrix[j][len(image_matrix) - 1 - i] = columnA[j]

    # Reflection about y = -x is like swapping diagonal elements:
    for i in range(len(image_matrix)):
        for j in range(len(image_matrix)):
            if i < j:                # Can ignore the Xs: [[X b c d],
                temp = image_matrix[j][i]               #  [X X g h],
                image_matrix[j][i] = image_matrix[i][j] #  [X X X l],
                image_matrix[i][j] = temp               #  [X X X X]]

    return image_matrix

print(rotate_cc([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
print(rotate_cc([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))
print(rotate_cc([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]))

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
