"""
Given an n x m array where all rows and columns are in sorted order, write a
function to determine whether the array contains an element x.
"""

def contains(arr, x):
    n = len(arr)
    if n == 0 or len(arr[0]) == 0:
        return False
    row =  0
    col =   n - 1


    while row < n and col >= 0 :

        if arr[row][col] == x:
            return True

        if arr[row][col]  < x :
            row +=1
        else:
            col -=1   

    return False    

arr = [[2,5,7,8],[0,1,6,8],[3,58,89,90]]   
x =  contains(arr, 89)
print(x)     

