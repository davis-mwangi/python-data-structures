"""
Given a 2D array of 1s and 0s, find the largest square subarray of all 1s.

subarray([​ 1 ​ , 1, 1, 0]
         [​ 1 ​ , 1, 1, 1]
         [​ 1 ​ , 1, 0, 0]) = ​ 2
"""
def subarray(arr):
    x =  len(arr)
    if x == 0:
        return 0
    
    y = len(arr[0])
    if y == 0:
        return 0
  
    max = 0       
    sizes = [[0 for i in range(y)] for i in range(x)]

    for i in range(x):
        for j in range(y):
            if i ==0 or j ==0:
                sizes[i][j]= arr[i][j]
            elif arr[i][j] == 1:
                sizes[i][j] = min(min(sizes[i][j-1],sizes[i-1][j]), sizes[i-1][j-1]) + 1
            if sizes[i][j] > max:
                max =  sizes[i][j]        

    return max

x = subarray([[1 ,1, 1, 0],
              [1 ,1, 1, 1],
              [1, 1, 0, 0]])
print(x)         