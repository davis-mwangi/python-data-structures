"""
Given two sorted arrays, a[] and b[], the task is to find the median of these sorted arrays, in O(log n + log m) time complexity, when n is the number of elements in the first array,
 and m is the number of elements in the second array.
"""
       
def median_arrays_diff_size(arr1, arr2):
    m =  len(arr1)
    n = len(arr2) 

    i = 0 # Current index of arr1[]
    j = 0 # current index of arr2[]
    count  = 0
    m1 = -1
    m2 = -1
    
    # case m+n is odd
    if (m + n) % 2 != 0:
        while count <= (m+n)/2 :
            if i != m and j != n:
                m1 = arr2[j +  1 ] if arr1[i] > arr2[j] else arr1[i + 1]
            elif i < m:
                m1 = arr1[i + 1]    
            else: # case j < n
                m1 = arr2[j + 1] 

            count +=1
            return m1
    else:  # case m+n =  even median  average ((m+n)/2 -) and (m+n)/2
        while count <= (n+m) / 2:
            m2 =  m1
            if i != n and j != m:
                m1 = arr2[ j + 1] if arr1[i] > arr2[j] else arr1[i + 1]   
            elif i < m:     
                m1 = arr1[i+1]
            else:
                m1 = arr2[j+1]   
            count +=1
        return   (m1 + m2)/2  

x = median_arrays_diff_size([900],[5, 8, 10, 20])
print(x)    
x = median_arrays_diff_size([1,2,3,4,5,6],[0,0,0,0,10,10])
print(x)

