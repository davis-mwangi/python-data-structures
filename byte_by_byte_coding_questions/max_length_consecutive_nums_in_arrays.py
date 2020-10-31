"""
Question​ : Given an unsorted array, find the length of the longest sequence of
consecutive numbers in the array.
"""
def consecutive(arr):
    set_x = set()
    set_x.update(arr) # add items to set t remove any duplicates

    max_len = 0
    for i in set_x:
        
        # if left most item do nothing
        if i-1 in set_x:
           continue
        length = 0
        while i in set_x:
            length +=1
            i+=1
        max_len =  max(max_len,length)  

    return max_len       


x = consecutive([4,2,1,6,5, 5, 20,21,22,24,23,25])    
print(x)
