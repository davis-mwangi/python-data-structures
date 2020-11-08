"""
Given 2 sorted arrays, A and B, where A is long enough to hold the contents of
A and B, write a function to copy the contents of B into A without using any buffer or
additional memory.

A = {​ 1 ​ , ​ 3 ​ , ​ 5 ​ , ​ 0 ​ , ​ 0 ​ , ​ 0 ​ }
B = {​ 2 ​ , ​ 4 ​ , ​ 6 ​ }
mergeArrays(A, B)
A = {​ 1 ​ , ​ 2 ​ , ​ 3 ​ , ​ 4 ​ , ​ 5 ​ , ​ 6 ​ }
"""
def mergeArrays(arr1, arr2, a_length, b_length):
    if (a_length + b_length) > len(arr1):
       raise Exception("Size of array exceeded")

    a_index = a_length -1
    b_index =  b_length - 1
    merge_index = (a_index + b_index) - 1

    while (a_index >= 0 and b_index >=0 ):
        if arr1[a_index] > arr2[b_index]:
            arr1[merge_index] =  arr1[a_index]
            a_index -= 1
        else:
            arr1[merge_index] =  arr2[b_index]
            b_index -= 1

        merge_index -= 1

    while b_index >= 0:
        arr1[merge_index] =  arr2[b_index]
        b_index -= 1
        merge_index -= 1   
    print(arr1)             


mergeArrays([1,3,5,0,0,0], [2,4,6], 3, 3 )
   

