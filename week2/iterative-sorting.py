### Objective challenge:
### 1. Try writing a Python function to perform a linear search on a set of data.
### 2. Try writing a Python function to perform a binary search on a set of data.
### 3. Can you rewrite the above function so that it uses recursion?

test_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# 1)
def linear_search(arr, target):
    steps = 1
    for i, num in enumerate(arr):
        if num == target:
            return {
                'index': i,
                'steps': steps
            }
        
        steps += 1
    
    return {
        'index': None,
        'steps': steps
    }

print(linear_search(test_data, 10)) # Expect: {'index': 10, 'steps': 11}

# 2)
def binary_search(arr, target):
    left_index = 0
    right_index = len(arr) - 1
    steps = 1

    while left_index != right_index:
        middle_index = left_index + ( (right_index - left_index) // 2 )

        if arr[middle_index] == target:
            return {
                'index': middle_index,
                'steps': steps
            }
        else:
            if arr[middle_index] > target:
                right_index = middle_index
            else: 
                left_index = middle_index + 1

        steps += 1

    return {
        'index': None,
        'steps': steps
    }

print(binary_search(test_data, 10))

# 3)
def recursive_binary_search(arr, target, left_index_offset = 0, steps = 1):
    left_index = 0
    right_index = len(arr) - 1

    middle_index = left_index + ( (right_index - left_index) // 2 )

    # Not sure if try-catch was the best way to handle targets which don't exist in arr, but it works!
    try:
        if arr[middle_index] == target:
            return {
                'index': left_index_offset + middle_index,
                'steps': steps
            }
        elif arr[middle_index] > target:
            return recursive_binary_search(arr[:middle_index], target, left_index_offset, steps + 1)
        else: 
            return recursive_binary_search(arr[middle_index + 1:], target, left_index_offset + middle_index + 1, steps + 1)
    except:
        return {
            'index': None,
            'steps': steps
        }

print(recursive_binary_search(test_data, 10))
print(recursive_binary_search(test_data, 20))

### Objective challenge:
### 1. What will the array [25, 67, 4, 33, 19, 40] look like after each pass of the Selection Sort algorithm?
### 2. What will the same array look like after each pass of the Insertion Sort algorithm?

# 1) 0th: [25, 67, 4, 33, 19, 40]
#    1st: [4, 67, 25, 33, 19, 40]
#    2nd: [4, 19, 25, 33, 67, 40]
#    3rd: [4, 19, 25, 33, 67, 40]
#    4th: [4, 19, 25, 33, 67, 40]
#    5th: [4, 19, 25, 33, 40, 67]

# 2) 0th: [25, 67, 4, 33, 19, 40]
#    1st: [25, 67, 4, 33, 19, 40]
#    2nd: [4, 25, 67, 33, 19, 40]
#    3rd: [4, 25, 33, 67, 19, 40]
#    4th: [4, 19, 25, 33, 67, 40]
#    5th: [4, 19, 25, 33, 40, 67]
