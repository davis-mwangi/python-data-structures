# Find the meridian of arrays of same size
def median_array_same_size(arr1,arr2):
    n  = len(arr1)
    i =  0 # current index of arr1[]
    j =  0 # current index of arr2[]
    m1 = -1
    m2 = -1
    count = 0
    while count < n + 1:
        count += 1
        if i == n:
            m1 = m2
            m2 = arr2[0]
            break
        elif j == n:
            m1 =  m2
            m2 = arr1[0]
            break
        if arr1[i] <= arr2[j]:
            m1 =  m2 # store the prec median
            m2 =  arr1[i]
            i += 1
        else:
            m1 =  m2
            m2 = arr2[j] 
            j += 1
    return (m1 +m2)/2           
x =  median_array_same_size([1,12,15,26,38],[2,13,17,30,46])
print(x)

# Time complexity O(n)

