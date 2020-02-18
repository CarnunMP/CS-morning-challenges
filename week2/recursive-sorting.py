### Objective challenge:
### 1. Write a recursive search function that receives as input an array of integers and a target integer value. This function should return True if the target element exists in the array, and False otherwise.
### 2. What would be the base case(s) we’d have to consider for implementing this function?
### 3. How should our recursive solution converge on our base case(s)?

### Objective challenge:
### 1. What will the contents of the array below be after each pass of the Merge Sort algorithm? merge-challenge
### 2. What will the contents of the array below be after each pass of the Quick Sort algorithm? (assume the first element is chosen as the pivot)

# 1) 0th: [39, 51, 7, 14, 3, 86]
#    1st: [39, 51, 7] [14, 3, 86]
#    2nd: [39, 51] [7] [14, 3] [86]
#    3rd: [39] [51] [7] [14] [3] [86]
#    4th: [39, 51] [7] [3, 14] [86]
#    5th: [7, 39, 51] [3, 14, 86]
#    6th: [3, 7, 14, 39, 51, 86]

# 2) 0th: [24, 44, 12, 99, 3, 56]
#    1st: [12, 3, 24, 44, 99, 56]
#    2nd: [3, 12, 24, 44, 99, 56]
#    3rd: [3, 12, 24, 44, 99, 56]
#    4th: [3, 12, 24, 44, 56, 99]